# coding: utf-8

"""
Parse user input to have exploitable data to send to APIs.
"""
import json
import re
import unicodedata as uc

from logger.logger import logger

logger.debug("test")


class Parser:
    """ Parse input data."""

    def __init__(self):
        self.stop_word_list = []

    # 1. lower_case
    # 2. accent_removal
    # 3. split_text_in_sentence
    # 4. stop_word_removal
    #
    #

    def split_text_in_sentences(self, text: str) -> list:
        """ Returns a list of string(multiple words) from input"""
        if len(re.split(r"\?", text)) > 2:
            return False
        sentence_list = re.split(r"; |, |\*|! |\n", text)
        return sentence_list

    def accent_removal(self, text: str) -> str:
        """ Return a string without accent"""
        text = uc.normalize('NFKD', text).encode('ASCII', 'ignore').decode(
            'ASCII')
        return text.lower()

    # TEST ?
    def get_keywords(self):
        self.stop_word_list = []
        with open("data/fr.json", encoding="utf-8") as file:
            data = json.load(file)
            for word in data:
                word = self.accent_removal(word)
                lister.append(word)
        return self.stop_word_list

    def stop_words_removal(self, sentence_list):
        relevant_word_list = []
        for word in sentence_list:
            if word not in self.stop_word_list:
                relevant_word_list.append(word)
        return relevant_word_list


a = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir Au " \
    "fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le " \
    "musée d'art et d'histoire de Fribourg, s'il te plaît? "
b = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que " \
    "tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et " \
    "salutations à Mamie. "
c = "Salut GrandPy ! Par hasard, est-ce que tu connais l'adresse " \
    "d'OpenClassrooms ?"
d = "à être içi l'hôte sur une île"

lister = [a, b, c, d]
gr = Parser()
# for i in lister:
#     print(gr.accent_removal("elles-mêmes"))


good = gr.accent_removal(a)
good = gr.split_text_in_sentences(good)

print(gr.stop_words_removal(good))
