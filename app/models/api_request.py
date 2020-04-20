""" This will handle any API request."""
import json

import requests

from app.config import config as cfg
from app.logger import logger

logger.debug("test")


class GoogleRequest:
    """Will handle the request for Google API."""

    def __init__(self, query):
        self.url = cfg.GOOGLE_API_URL
        self.key = None
        self.query = query.split()
        self.query = "+".join(self.query)

    def api_request(self):
        self.key = self._get_api_key("google")
        url = f"{self.url}address={self.query}&key={self.key}"
        lat, lon = None, None
        try:
            logger.info(f"Handling google API request {self.query}")
            req = requests.get(url)
            resp_json = req.json()
            lat = resp_json['results'][0]['geometry']['location'][
                'lat']
            lon = resp_json['results'][0]['geometry']['location'][
                'lng']
            logger.info(f"Return google API result")
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"Exception HTTPError : {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            logger.error(f"Exception Connection Error {conn_err}")
        except requests.exceptions.Timeout as tmout_err:
            logger.error(f"Exception Timeout : {tmout_err}")
        except requests.exceptions.RequestException as err:
            logger.error(f"Unknown Error: {err}")
        return lat, lon

    def _get_api_key(self, api: str) -> str:
        key = None
        try:
            with open("app/config/api_key.json") as file:
                data = json.load(file)
                key = data["api"][api]
        except IOError as e:
            logger.error(f"IOError Opening Key file {e}")
        except ValueError as e:
            logger.error(f"ValueError Opening Key file {e}")
        except EOFError as e:
            logger.error(f"EOFError Opening Key file {e}")
        except Exception as e:
            logger.error(f"Exception Opening Key file {e}")
        return key


class WikipediaRequest:
    # https://www.mediawiki.org/wiki/API:Search#API_documentation
    def __init__(self, query):
        self.query = query

    def _id_request(self, keyword):
        payload = cfg.WIKI_PAYLOAD
        payload["srsearch"] = keyword
        req = requests.get(cfg.WIKI_API_URL, params=payload)
        resp_json = req.json()
        return str(resp_json["query"]["search"][0]["pageid"])

    def _extract_request(self, page_id):
        payload = cfg.WIKI_EX_PAYLOAD
        payload["pageids"] = page_id
        req = requests.get(cfg.WIKI_API_URL, params=payload)
        resp_json = req.json()
        return resp_json["query"]["pages"][page_id]["extract"]

    def api_request(self):
        page_id = self._id_request(self.query)
        extract = self._extract_request(page_id)
        return extract


if __name__ == "__main__":
    # gr = GoogleRequest("tour eiffel")
    # a = gr.api_request()
    # print("geocode is :", a)
    w = WikipediaRequest("tour eiffel")
    print(w.api_request())
