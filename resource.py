from files.duckduckgo import search


class GetResource:
    def __init__(self, resource, input_words):
        self.link = ""
        self.input_words = input_words
        function_to_call = getattr(self, "get_" + resource)
        function_to_call()

    def get_stack(self):
        self.link = ""

    def get_ddg(self):
        self.link = ""
        search(self.input_words, 5)

    def get_wiki(self):
        self.link = ""

    def get_docs(self):
        self.link = ""

    def get_api(self):
        self.link = ""
