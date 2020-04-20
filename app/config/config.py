# # Google Maps API basis
# MAP_API_KEY = os.environ['MAP_API_KEY']
# MAP_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
# MAP_PAYLOAD = {"input":"", "inputtype":"textquery",
#     "fields":"formatted_address,name,geometry", "key": MAP_API_KEY}
#
# # Wikipedia API basis
# WIKI_URL = "https://fr.wikipedia.org/w/api.php"
# WIKI_PAYLOAD = {"action":"query", "list":"search", "srsearch":"",
#     "utf8":"", "format":"json"}

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

WIKI_EX_PAYLOAD = {
    "action": "query",
    "pageids": None,
    "prop": "extracts",
    "explaintext": "true",
    "exsectionformat": "plain",
    "exsentences": "3",
    "format": "json"
}
