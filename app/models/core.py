import random as rd

from app.config import config as cfg
from app.models.api_request import GoogleRequest, WikipediaRequest
from app.models.parser import Parser


class Core:

    def __init__(self):
        """ Initialize  each Class used to process the input."""

        self.parser = Parser()
        self.google_req = GoogleRequest()
        self.wiki_req = WikipediaRequest()

    def process(self, text_input: str) -> dict:
        """ Process the user input and return a dictionary with full
        data associated.
        """
        data = self.parser.process(text_input)
        data = self.google_req.api_request(data)
        data = self.wiki_req.api_request(data)
        data = self._format_message(data)
        return data

    def _format_message(self, data):
        """ Format the answer."""

        start = rd.choice(cfg.START_SENTENCE)
        story = rd.choice(cfg.STORY_SENTENCE)
        message = f"{start}{data['address']}. \n" \
                  f"{story} \n" \
                  f"{data['page_id_article']}. \n" \
                  f"Pour en savoir plus visite ce lien :) \n" \
                  f"{data['url']}"
        data["formatted_message"] = message
        return data


if __name__ == '__main__':
    core = Core()
    print(core.process("Où se situe la tour Eiffel ?"))
