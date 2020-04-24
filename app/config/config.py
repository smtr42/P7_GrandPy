from dotenv import load_dotenv, find_dotenv
from os import getenv


def load_key():
    load_dotenv(find_dotenv())
    API_KEY = getenv('google_api')
    return API_KEY

STOP_WORD_PATH = "app/data/fr.json"

key_localisation = ['endroit', 'adresse', 'rue', 'lieu', 'place',
                    'coordonnées', 'localiser', 'où sont', 'où est',
                    'localisation', 'indiquer', 'se trouve', 'où',
                    'se situe', ]

GOOGLE_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?"
WIKI_API_URL = "https://fr.wikipedia.org/w/api.php"
WIKI_PAYLOAD = {
    "action": "query",
    "list": "search",
    "srsearch": None,
    "srlimit": "1",
    "format": "json"
}
WIKI_GEO_PAYLOAD = {
    "format": "json",
    "list": "geosearch",
    "gscoord": "",
    "gslimit": "10",
    "gsradius": "10000",
    "action": "query"
}
WIKI_EX_PAYLOAD = {
    "action": "query",
    "pageids": None,
    "prop": "extracts",
    "explaintext": "true",
    "exsectionformat": "plain",
    "exsentences": "3",
    "format": "json"
}

WIKI_URL_PAYLOAD = {
    "action": "query",
    "prop": "info",
    "pageids": None,
    "inprop": "url|talkid",
    "format": "json"
}