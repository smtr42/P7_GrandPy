import requests
from app.models.api_request import GoogleRequest


class MockResponse:
    def json(self):
        return {'results': [{
            'geometry': {
                'location': {'lat': 48.85837009999999, 'lng': 2.2944813}},
            "formatted_address": 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France'
        }], 'status': 'OK'}


class TestGoogleRequest:

    def setup_method(self):
        self.app = GoogleRequest()
        self.inter = {'error': False, 'input_raw': 'Où se trouve la tour Eiffel ?', 'input_loc': 'tour eiffel', 'formatted_message': '', 'no_result': "Désolé, je n'ai pas compris ta demande ou je ne connais pas ce lieu. Try again !", 'lat': 43.1, 'lon': 6.3, 'address': '', 'pageid': None, 'page_id_article': None, 'url': ''}
        self.outer = {'error': False, 'input_raw': 'Où se trouve la tour Eiffel ?', 'input_loc': 'tour eiffel', 'formatted_message': '', 'no_result': "Désolé, je n'ai pas compris ta demande ou je ne connais pas ce lieu. Try again !", 'lat': 48.85837009999999, 'lon': 2.2944813, 'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France', 'pageid': None, 'page_id_article': None, 'url': ''}

    def test_google_api_request(self, monkeypatch):
        def mock_get(url, *args, **kwargs):
            return MockResponse()
        monkeypatch.setattr(requests, "get", mock_get)
        assert self.app.api_request(self.inter) == self.outer
