from app.models.parser import Parser


class TestParser:

    def setup_method(self):
        self.parser = Parser()
        self.result = {"error": False,
                       "input_raw": "",
                       "input_loc": "",
                       "formatted_message": "",
                       "no_result": "Désolé, je n'ai pas compris ta demande"
                                    " ou je ne connais pas ce lieu."
                                    " Try again !",
                       "lat": 43.1,
                       "lon": 6.3,
                       "address": "",
                       "pageid": None,
                       "page_id_article": None,
                       "url": "",
                       }
        self.raw_sentence = "Bonsoir Grandpy, j'espère que tu as passé une " \
                            "belle semaine. Est-ce que tu pourrais " \
                            "m'indiquer l'adresse de la tour eiffel ? Merci " \
                            "d'avance et salutations à Mamie."

    def test_process(self):
        assert self.parser.process(self.raw_sentence) == {
            'error': False,
            'input_raw': "Bonsoir Grandpy, j'espère que tu as passé une belle"
                         " semaine. Est-ce que tu pourrais m'indiquer"
                         " l'adresse de la tour eiffel ? Merci d'avance et"
                         " salutations à Mamie.",
            'input_loc': 'tour eiffel',
            'formatted_message': '',
            'no_result': "Désolé, je n'ai pas compris ta demande ou je ne"
                         " connais pas ce lieu. Try again !",
            'lat': 43.1,
            'lon': 6.3,
            'address': '',
            'pageid': None,
            'page_id_article': None,
            'url': ''
        }
