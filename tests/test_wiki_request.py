import requests

from app.models.api_request import WikipediaRequest


class MockResponseExtract:
    def json(self, *args, **kwargs):
        return extract_request


class MockResponseUrl:
    def json(self, *args, **kwargs):
        return url_request


class MockResponseId:
    def json(self, *args, **kwargs):
        return id_request


class TestWikipediaRequest:

    def setup_method(self):
        self.app = WikipediaRequest()

    def mock_id_request(self, data, *args, **kwargs):
        data["pageid"] = 5422123
        return data

    def mock_url_request(self, data, *args, **kwargs):
        data["url"] = 'https://fr.wikipedia.org/wiki/Exposition_universelle_de_Paris_de_1889'
        return data

    def mock_extract_request(self, data, *args, **kwargs):
        data["page_id_article"] = "L'Exposition universelle de Paris de 1889 est la dixième Exposition universelle organisée. Elle se tient du 5 mai au 31 octobre 1889. Son thème est la Révolution française, dans le cadre du centenaire de cet événement."
        return data

    def test_extract_request(self, monkeypatch):
        # Mock ID
        monkeypatch.setattr(
            "app.models.api_request.WikipediaRequest._id_geo_request",
            self.mock_id_request)
        monkeypatch.setattr(
            "app.models.api_request.WikipediaRequest._url_request",
            self.mock_url_request)

        # Mock request de extract
        def get_mock(*args, **kwargs):
            return MockResponseExtract()

        monkeypatch.setattr(requests, "get", get_mock)
        assert self.app.api_request(data_start) == data_end

    def test_id_request(self, monkeypatch):
        # Mock ID
        monkeypatch.setattr(
            "app.models.api_request.WikipediaRequest._extract_request",
            self.mock_extract_request)
        monkeypatch.setattr(
            "app.models.api_request.WikipediaRequest._url_request",
            self.mock_url_request)

        # Mock request de extract
        def get_mock(*args, **kwargs):
            return MockResponseId()

        monkeypatch.setattr(requests, "get", get_mock)
        assert self.app.api_request(data_start) == data_end

    def test_url_request(self, monkeypatch):
        # Mock ID
        monkeypatch.setattr(
            "app.models.api_request.WikipediaRequest._extract_request",
            self.mock_extract_request)
        monkeypatch.setattr(
            "app.models.api_request.WikipediaRequest._id_geo_request",
            self.mock_id_request)

        # Mock request de extract
        def get_mock(*args, **kwargs):
            return MockResponseUrl()

        monkeypatch.setattr(requests, "get", get_mock)
        assert self.app.api_request(data_start) == data_end



data_start = {'error': False, 'input_raw': 'Où se trouve la tour Eiffel ?',
              'input_loc': 'tour eiffel', 'formatted_message': '',
              'no_result': "Désolé, je n'ai pas compris ta demande ou je ne connais pas ce lieu. Try again !",
              'lat': 48.85837009999999, 'lon': 2.2944813,
              'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
              'pageid': None, 'page_id_article': None, 'url': ''}
data_end = {'error': False, 'input_raw': 'Où se trouve la tour Eiffel ?',
            'input_loc': 'tour eiffel', 'formatted_message': '',
            'no_result': "Désolé, je n'ai pas compris ta demande ou je ne connais pas ce lieu. Try again !",
            'lat': 48.85837009999999, 'lon': 2.2944813,
            'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
            'pageid': 5422123,
            'page_id_article': "L'Exposition universelle de Paris de 1889 est la dixième Exposition universelle organisée. Elle se tient du 5 mai au 31 octobre 1889. Son thème est la Révolution française, dans le cadre du centenaire de cet événement.",
            'url': 'https://fr.wikipedia.org/wiki/Exposition_universelle_de_Paris_de_1889'}

id_request = {'query': {'geosearch': [{'pageid': 5422123}]}}
extract_request = {'query': {'pages': {'5422123': {
    'extract': "L'Exposition universelle de Paris de 1889 est la dixième Exposition universelle organisée. Elle se tient du 5 mai au 31 octobre 1889. Son thème est la Révolution française, dans le cadre du centenaire de cet événement."}}}}
url_request = {'query': {'pages': {
    '5422123': {'fullurl': 'https://fr.wikipedia.org/wiki/Exposition_universelle_de_Paris_de_1889'}}}}
