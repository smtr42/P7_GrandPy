""" This will handle any API request."""

import random

import requests

from app.config import config as cfg
from app.logger.logger import logger


class GoogleRequest:
    """Will handle the request for Google API."""

    def __init__(self):
        self.url = cfg.GOOGLE_API_URL
        self.key = cfg.load_key()

    def api_request(self, data: dict) -> dict:
        """The main public method : handle the input and return all
         geo data associated.
         """

        query = data["input_loc"]
        query = query.split()
        query = "+".join(query)
        # self.key = self._get_api_key("google")
        url = f"{self.url}address={query}&key={self.key}"
        result = {"address": None, "lat": None, "lon": None}
        try:
            logger.info(f"Handling google API request {query}")
            req = requests.get(url)
            resp_json = req.json()
            result["lat"] = resp_json['results'][0]['geometry']['location'][
                'lat']
            result["lon"] = resp_json['results'][0]['geometry']['location'][
                'lng']
            result["address"] = resp_json['results'][0]["formatted_address"]

            logger.info(f"Return google API result")
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"Exception HTTPError : {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            logger.error(f"Exception Connection Error {conn_err}")
        except requests.exceptions.Timeout as tmout_err:
            logger.error(f"Exception Timeout : {tmout_err}")
        except requests.exceptions.RequestException as err:
            logger.error(f"Unknown Error: {err}")
        result = {**data, **result}
        return result


class WikipediaRequest:
    # https://www.mediawiki.org/wiki/API:Search#API_documentation
    def _id_geo_request(self, data: dict):
        """Return a random pageid from places around given geo coordinates."""

        lat, lon = round(data["lat"], 7), round(data["lon"], 7)
        payload = cfg.WIKI_GEO_PAYLOAD
        payload["gscoord"] = f"{lat}|{lon}"
        req = requests.get(cfg.WIKI_API_URL, params=payload)
        resp_json = req.json()
        place = random.choice(resp_json["query"]["geosearch"])
        data["pageid"] = place["pageid"]
        return data

    def _extract_request(self, data: dict) -> dict:
        """Return an desription of the place from the pageid and its url."""

        pageid = data["pageid"]
        payload = cfg.WIKI_EX_PAYLOAD
        payload["pageids"] = pageid
        req = requests.get(cfg.WIKI_API_URL, params=payload)
        resp_json = req.json()
        data["page_id_article"] = resp_json["query"]["pages"][str(pageid)][
            "extract"]
        return data

    def _url_request(self, data: dict) -> dict:
        """Get the url from the associated pageid."""

        pageid = data["pageid"]
        payload = cfg.WIKI_URL_PAYLOAD
        payload["pageids"] = pageid
        req = requests.get(cfg.WIKI_API_URL, params=payload)
        resp_json = req.json()
        data["url"] = resp_json["query"]["pages"][str(pageid)][
            "fullurl"]
        return data

    def api_request(self, data: dict) -> dict:
        """Public method gathering each mediawiki data."""

        data = self._id_geo_request(data)
        data = self._extract_request(data)
        data = self._url_request(data)
        return data


if __name__ == "__main__":
    r = {"input_loc": "tour eiffel", "lat": 48.85837009999999,
         "lon": 2.2944813}
    k = GoogleRequest()
    print(k.api_request(r))

    #
    # h = {"input_loc": "tour eiffel", "lat": 48.85837009999999,
    #      "lon": 2.2944813}
    # w = WikipediaRequest()
    # print(w.api_request(h))
