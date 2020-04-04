

# Google Maps API basis
MAP_API_KEY = os.environ['MAP_API_KEY']
MAP_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
MAP_PAYLOAD = {"input":"", "inputtype":"textquery",
    "fields":"formatted_address,name,geometry", "key": MAP_API_KEY}

# Wikipedia API basis
WIKI_URL = "https://fr.wikipedia.org/w/api.php"
WIKI_PAYLOAD = {"action":"query", "list":"search", "srsearch":"",
    "utf8":"", "format":"json"}