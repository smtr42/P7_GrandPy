""" This will handle any API request."""
import requests

import config.config as cfg
from logger.logger import logger

logger.debug("test")


class GoogleRequest:
    """Will handle the request for Google API."""

    def __init__(self, query):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?address="
        self.key = None
        self.query = query.split()
        self.query = "+".join(self.query)

    def api_request(self):
        url = f"{self.url}{self.query}&key={cfg.GOOGLE_API_KEY}"
        lat, lon = 0, 0
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

    def format_query(self):
        pass

    def filter(self):
        pass

    def get_api_key(self):
        pass


class GoogleGeoCode:
    """Format the API answer into useful data."""

    def __init__(self):
        pass


class WikipediaRequest:
    pass


if __name__ == "__main__":
    gr = GoogleRequest("tour eiffel")
    a = gr.api_request()
    print(a)
