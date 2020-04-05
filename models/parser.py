# coding: utf-8

"""
Parse user input to have exploitable data to send to APIs.
"""
import json
import re
import unicodedata as uc

import config.config as cfg
from logger.logger import logger

logger.debug("test")


class Parser:
    """ Parse input data."""

    def __init__(self):
        self._stop_word_list = []
        self.result = ""

    def process(self, raw_sentence):

        self._stop_word_list = self._get_keywords()
        sentence_list = self._split_text_in_sentences(raw_sentence)
        relevant_sentence = self._extract_relevant_info(sentence_list)
        relevant_cleaned = self._special_removal(relevant_sentence)
        self.result = self._stop_words_removal(relevant_cleaned,
                                               self._stop_word_list)
        return self.result

    def _get_keywords(self):
        """ Get the storpwords from the json files."""
        word_list = []
        try:
            with open(cfg.STOP_WORD_PATH, encoding="utf-8") as file:
                data = json.load(file)
                for word in data:
                    word = self._accent_removal(word)
                    word_list.append(word)
        except EOFError as EOF:
            logger.error(
                f"EOFError while opening the file {cfg.STOP_WORD_PATH} : {EOF}")
        except IOError as e:
            logger.error(
                f"IOError while opening the file {cfg.STOP_WORD_PATH} : {e}")
        except Exception as exc:
            logger.error(
                f"IOError while opening the file {cfg.STOP_WORD_PATH} : {exc}")
        finally:
            return word_list

    def _split_text_in_sentences(self, text):
        """Splits text in sentences to narrow the search"""
        return re.split(r"; |, |\*|! |\n", text)

    def _extract_relevant_info(self, sentence_list):
        """ Search for localisation word to locate the relevant text."""
        for sentence in sentence_list:
            raw_relevant = re.findall(
                r"(?=(" + '|'.join(cfg.key_localisation) + r"))",
                sentence.lower())
            if raw_relevant:
                first_half, middle, second_half = sentence.rpartition(
                    raw_relevant[-1])
                for p in "?!.":
                    if p in second_half:
                        good, punctuation, to_delete = second_half.partition(p)
                        return good
                        break
                    else:
                        return second_half
        return ""

    def _accent_removal(self, text):
        """ Return a string without accent"""
        text = uc.normalize('NFKD', text).encode('ASCII', 'ignore').decode(
            'ASCII')
        return text.lower()

    def _special_removal(self, relevant_sentence):
        """ Remove special characters and punctuation"""
        de_accentized = self._accent_removal(relevant_sentence)
        de_punctuated = re.sub('[!@#$?,:;.]', '', de_accentized)
        de_apostrophed = re.sub(r'(\s|^)\w{1}\'', ' ', de_punctuated)
        return de_apostrophed

    def _stop_words_removal(self, relevant_cleaned, stop_word_list) -> str:
        sentence = relevant_cleaned.split()
        final = " ".join([word for word in sentence if
                          word not in stop_word_list])
        return final


if __name__ == "__main__":
    instance = Parser()
    i = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que " \
        "tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et " \
        "salutations à Mamie. "
    print("final process :", instance.process(i))
