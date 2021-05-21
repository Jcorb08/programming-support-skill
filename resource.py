from .duckduckgo import search
from mycroft.util.log import LOG


# creates a new object using the resource retrieved from action
# and the input words or intent from action also.
# calls the function that is the same as the resource inputted
# resource = 'ddg' then its get_ddg() called.
class GetResource:
    def __init__(self, resource, input_words):
        self.link = ""
        self.input_words = input_words
        function_to_call = getattr(self, "get_" + resource)
        function_to_call()

    def get_stack(self):
        # !bangs - !stackoverflow at start of request
        # gives multiple potential answers
        # sets link to stack overflow and searches using input_words.
        self.link = "https://duckduckgo.com/?q=!stackoverflow " + self.input_words

    def get_ddg(self):
        # fallback
        # searches using duckduckgo usaing input_words
        self.link = "https://duckduckgo.com/?q=" + self.input_words

    def get_wiki(self):
        # !bangs - !wikipedia at start
        # gives direct document
        # even though link is search the term should give correct doc
        # sets link to wikipedia and searches using input_words.
        self.link = "https://duckduckgo.com/?q=!wikipedia " + self.input_words

    def get_docs(self):
        # !bangs - just !java11 at mo
        # searches ddg using library above and picks the top result
        # sets this to be the link
        search_term = "!java11 " + (self.input_words.removesuffix('+java'))
        gen = search(search_term, max_results=2)
        for s in gen:
            LOG.debug("search link", s)
            self.link = s

    def get_api(self):
        # q here is search term for database
        # grabs relevant doc to display on website api
        # set link to website api and search term is input_words
        self.link = "https://programmingsupport.ml/?q=" + self.input_words
        # link below was when it was local testing
        # self.link = "http://localhost:8000/?q=" + self.input_words