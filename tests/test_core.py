from app.models.core import Core


class MockResponseParser:
    def process(self, text_input, *args, **kwargs):
        parser_return["input_raw"] = text_input
        return parser_return


class MockResponseGoogleRequest:
    def api_request(self, data, *args, **kwargs):
        data = {**data, **google_req_return}
        print(data)
        return data


class TestCore:

    def setup_method(self):
        self.core = Core()

    def mock_format_message(self, data, *args, **kwargs):
        message = f"Très bonne question, l'adresse est ici :" \
                  f" {data['address']}. \n" \
                  f"Oh mais il y a ce lieu à ne pas manquer" \
                  f" à deux pas de là.  \n" \
                  f"{data['page_id_article']}. \n" \
                  f"Pour en savoir plus visite ce lien :) \n" \
                  f"{data['url']}"
        data["formatted_message"] = message
        return data

    def test_core_format(self, monkeypatch):
        def get_w_mock(data, *args, **kwargs):
            data = {**data, **wiki_req_return}
            return data

        monkeypatch.setattr(self.core.wiki_req, "api_request", get_w_mock)

        def get_g_mock(data, *args, **kwargs):
            data = {**data, **google_req_return}
            return data

        monkeypatch.setattr(self.core.google_req, "api_request", get_g_mock)

        monkeypatch.setattr(
            "app.models.core.Core._format_message",
            self.mock_format_message)

        assert self.core.process(text_input) == _format_message_return


text_input = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine." \
             " Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel" \
             " ? Merci d'avance et salutations à Mamie."
parser_return = {'error': False,
                 'input_raw': "Bonsoir Grandpy, j'espère que tu as passé une"
                              " belle semaine. Est-ce que tu pourrais"
                              " m'indiquer l'adresse de la tour eiffel ?"
                              " Merci d'avance et salutations à Mamie.",
                 'input_loc': 'tour eiffel', 'formatted_message': '',
                 'no_result': "Désolé, je n'ai pas compris ta demande ou je"
                              " ne connais pas ce lieu. Try again !",
                 'lat': 43.1, 'lon': 6.3, 'address': '', 'pageid': None,
                 'page_id_article': None, 'url': ''}
google_req_return = {'error': False,
                     'input_raw': "Bonsoir Grandpy, j'espère que tu as passé"
                                  " une belle semaine. Est-ce que tu pourrais"
                                  " m'indiquer l'adresse de la tour eiffel ?"
                                  " Merci d'avance et salutations à Mamie.",
                     'input_loc': 'tour eiffel', 'formatted_message': '',
                     'no_result': "Désolé, je n'ai pas compris ta demande ou"
                                  " je ne connais pas ce lieu. Try again !",
                     'lat': 48.85837009999999, 'lon': 2.2944813,
                     'address': 'Champ de Mars, 5 Avenue Anatole France, 75007'
                                ' Paris, France',
                     'pageid': None,
                     'page_id_article': None, 'url': ''}
wiki_req_return = {'error': False,
                   'input_raw': "Bonsoir Grandpy, j'espère que tu as passé"
                                " une belle semaine. Est-ce que tu pourrais"
                                " m'indiquer l'adresse de la tour eiffel ?"
                                " Merci d'avance et salutations à Mamie.",
                   'input_loc': 'tour eiffel', 'formatted_message': '',
                   'no_result': "Désolé, je n'ai pas compris ta demande ou"
                                " je ne connais pas ce lieu. Try again !",
                   'lat': 48.85837009999999, 'lon': 2.2944813,
                   'address': 'Champ de Mars, 5 Avenue Anatole France, 75007'
                              ' Paris, France',
                   'pageid': 5422039,
                   'page_id_article': "L'allée Paul-Deschanel est une voie du"
                                      " 7e arrondissement de Paris, en"
                                      " France.\n\n\nSituation et"
                                      " accès\nL'allée Paul-Deschanel est une"
                                      " voie publique située dans le 7e"
                                      " arrondissement de Paris. Elle débute"
                                      " au 67, quai Branly et se termine"
                                      " avenue Silvestre-de-Sacy.",
                   'url': 'https://fr.wikipedia.org/'
                          'wiki/All%C3%A9e_Paul-Deschanel'}
_format_message_return = {'error': False,
                          'input_raw': "Bonsoir Grandpy, j'espère que tu as"
                                       " passé une belle semaine. Est-ce que"
                                       " tu pourrais m'indiquer l'adresse de"
                                       " la tour eiffel ? Merci d'avance et"
                                       " salutations à Mamie.",
                          'input_loc': 'tour eiffel',
                          'formatted_message': "Très bonne question,"
                                               " l'adresse est ici : Champ de"
                                               " Mars, 5 Avenue Anatole"
                                               " France, 75007 Paris, France."
                                               " \nOh mais il y a ce lieu à"
                                               " ne pas manquer à deux pas de"
                                               " là.  \nL'allée Paul-Deschanel"
                                               " est une voie du 7e"
                                               " arrondissement de Paris, en"
                                               " France.\n\n\nSituation et"
                                               " accès\nL'allée Paul-Deschanel"
                                               " est une voie publique située"
                                               " dans le 7e arrondissement de"
                                               " Paris. Elle débute au 67,"
                                               " quai Branly et se termine"
                                               " avenue Silvestre-de-Sacy"
                                               ".. \nPour en savoir plus"
                                               " visite ce lien :) \nhttps:"
                                               "//fr.wikipedia.org/wiki/"
                                               "All%C3%A9e_Paul-Deschanel",
                          'no_result': "Désolé, je n'ai pas compris ta demande"
                                       " ou je ne connais pas ce lieu."
                                       " Try again !",
                          'lat': 48.85837009999999, 'lon': 2.2944813,
                          'address': 'Champ de Mars, 5 Avenue Anatole France,'
                                     ' 75007 Paris, France',
                          'pageid': 5422039,
                          'page_id_article': "L'allée Paul-Deschanel est une"
                                             " voie du 7e arrondissement de"
                                             " Paris, en France.\n\n\n"
                                             "Situation et accès\nL'allée"
                                             " Paul-Deschanel est une voie"
                                             " publique située dans le 7e"
                                             " arrondissement de Paris. Elle"
                                             " débute au 67, quai Branly et"
                                             " se termine avenue"
                                             " Silvestre-de-Sacy.",
                          'url': 'https://fr.wikipedia.org/wiki/All%C3%A9e_'
                                 'Paul-Deschanel'}
