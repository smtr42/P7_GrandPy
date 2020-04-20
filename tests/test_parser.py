from parser import Parser


class TestParser:

    def setup_method(self):
        self.parser = Parser()
        self.a_text = "Salut grandpy! Comment s'est passé ta soirée avec " \
                      "Grandma hier soir? Au fait, pendant que j'y pense, " \
                      "pourrais-tu m'indiquer où se trouve le musée d'art et " \
                      "d'histoire de Fribourg, s'il te plaît? "

        self.b_text = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que " \
                      "tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et " \
                      "salutations à Mamie. "
        self.c_text = "Salut GrandPy ! Par hasard, est-ce que tu connais l'adresse " \
                      "d'OpenClassrooms ?"

    def test_split_text_in_sentences(self):
        assert len(self.parser._split_text_in_sentences(self.a_text)) == 5
        assert self.parser._split_text_in_sentences(self.a_text) == \
               ['Salut grandpy',
                "Comment s'est passé ta soirée avec Grandma hier soir? "
                "Au fait",
                "pendant que j'y pense",
                "pourrais-tu m'indiquer où se trouve le musée d'art et "
                "d'histoire de Fribourg",
                "s'il te plaît? "]

    def test_extract_relevant_info(self):
        first = ['Salut grandpy',
                 "Comment s'est passé ta soirée avec Grandma hier soir?"
                 " Au fait",
                 "pendant que j'y pense",
                 "pourrais-tu m'indiquer où se trouve le musée d'art et "
                 "d'histoire de Fribourg",
                 "s'il te plaît? "]
        assert self.parser._extract_relevant_info(
            first) == " le musée d'art et d'histoire de Fribourg"
        second = ['Bonsoir Grandpy',
                  "j'espère que tu as passé une belle semaine. Est-ce que tu "
                  "pourrais m'indiquer l'adresse de la tour eiffel? Merci "
                  "d'avance et salutations à Mamie. "]
        assert self.parser._extract_relevant_info(
            second) == " de la tour eiffel"

    def test_accent_removal(self):
        first = "içi, là où l'élève jeûne"
        assert self.parser._accent_removal(first) == "ici, la ou l'eleve jeune"

    def test_special_removal(self):
        first = "l'élève ! $."
        assert self.parser._special_removal(first) == " eleve  "

    def test_stop_words_removal(self):
        first = "qui dort rarement"
        assert self.parser._stop_words_removal(first,
                                               self.parser._get_keywords()) == "dort"
