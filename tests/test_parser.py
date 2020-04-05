from models.parser import Parser

a = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au " \
    "fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le " \
    "musée d'art et d'histoire de Fribourg, s'il te plaît? "
b = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que " \
    "tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et " \
    "salutations à Mamie. "
c = "Salut GrandPy ! Par hasard, est-ce que tu connais l'adresse " \
    "d'OpenClassrooms ?"


class TestParser:

    def setup_method(self):
        self.parser = Parser()
        self.raw_text = "Salut GrandPy ! Par hasard, est-ce que tu connais l'adresse " \
                        "d'OpenClassrooms ? "

    def test_split_text_in_sentences(self):
        assert len(self.parser.split_text_in_sentences(self.raw_text)) == 3
        assert self.parser.split_text_in_sentences(
            self.raw_text) == ['Salut GrandPy ', 'Par hasard',
                               "est-ce que tu connais l'adresse "
                               "d'OpenClassrooms ? "]
        assert (self.parser.split_text_in_sentences("? ?") == (not True))

    def test_accent_removal(self):
        assert self.parser.accent_removal(
            "à être içi l'hôte sur une île") == "a etre ici l'hote sur une ile"

    # def test_stop_words_removal(self):
    #     assert self.parser.stop_words_removal("la maison") == "maison"