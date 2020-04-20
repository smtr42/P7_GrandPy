import requests
from app.models import GoogleRequest


class MockResponse:
    def json(self):
        return {'results': [{
            'geometry': {
                'location': {'lat': 48.85837009999999, 'lng': 2.2944813}}
        }], 'status': 'OK'}


class TestGoogleRequest:

    def setup_method(self):
        self.app = GoogleRequest("tour eiffel")

    def test_google_api_request(self, monkeypatch):
        def mock_get(url, *args, **kwargs):
            return MockResponse()
        monkeypatch.setattr(requests, "get", mock_get)
        assert self.app.api_request() is not (None, None)



