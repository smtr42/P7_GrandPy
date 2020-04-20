import requests

from app.models import WikipediaRequest


class MockResponseExtract:
    def json(self, *args, **kwargs):
        return extract_request


class TestWikipediaRequest:

    def setup_method(self):
        self.app = WikipediaRequest("tour eiffel")

    def mock_id_request(self, *args, **kwargs):
        return str(1359783)

    def test_extract_request(self, monkeypatch):
        # Mock ID
        monkeypatch.setattr("models.api_request.WikipediaRequest._id_request",
                            self.mock_id_request)

        # Mock request de extract
        def get_mock(*args, **kwargs):
            return MockResponseExtract()

        monkeypatch.setattr(requests, "get", get_mock)

        assert self.app.api_request() == "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France. Construite par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », ce monument est devenu le symbole de la capitale française, et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 6,9 millions de visiteurs, en 2011 la cathédrale Notre-Dame de Paris était en tête des monuments à l'accès libre avec 13,6 millions de visiteurs estimés mais il reste le monument payant le plus visité au monde,."

    def test_id_request(self, monkey):
        pass

id_request = {'query': {'search': [{'pageid': 1359783}]}}

extract_request = {'query': {'pages': {'1359783': {
    'extract': "La tour Eiffel  est une tour de fer puddlé de 324 mètres de "
               "hauteur (avec antennes) située à Paris, à l’extrémité "
               "nord-ouest du parc du Champ-de-Mars en bordure de la Seine"
               " dans le 7e arrondissement. Son adresse officielle est 5,"
               " avenue Anatole-France. Construite par Gustave Eiffel et ses"
               " collaborateurs pour l’Exposition universelle de Paris de"
               " 1889, et initialement nommée « tour de 300 mètres », ce"
               " monument est devenu le symbole de la capitale française,"
               " et un site touristique de premier plan : il s’agit du"
               " troisième site culturel français payant le plus visité en"
               " 2015, avec 6,9 millions de visiteurs, en 2011 la cathédrale"
               " Notre-Dame de Paris était en tête des monuments à l'accès"
               " libre avec 13,6 millions de visiteurs estimés mais il reste"
               " le monument payant le plus visité au monde,."}}}}
