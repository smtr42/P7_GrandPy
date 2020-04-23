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
        payload = self.parser.process(text_input)
        payload = self.google_req.api_request(payload)
        payload = self.wiki_req.api_request(payload)
        return payload


if __name__ == '__main__':
    core = Core()
    print(core.process("Où se situe la tour Eiffel ?"))
