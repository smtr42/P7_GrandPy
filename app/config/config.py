from os import getenv

from dotenv import load_dotenv, find_dotenv


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

START_SENTENCE = ["Alors voilà l'adresse mon ptit gars : ",
                  "Ah ça y est je me souviens c'est ici : ",
                  "Mmhh, voyons voir ça devrait être ici : ",
                  "Très bonne question, l'adresse est ici : ",
                  ]

STORY_SENTENCE = ["Au fait, je t'ai raconté mon anecdote près de là ? ",
                  "Ah ça me rappel cet endroit pas très loin. ",
                  "Y a cet endroit sympa tout proche de là je me souviens. ",
                  "Oh mais il y a ce lieu à ne pas manquer à deux pas de là. "]

