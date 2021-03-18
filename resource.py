from .duckduckgo import search
from mycroft.util.log import LOG


class GetResource:
    def __init__(self, resource, input_words):
        self.link = ""
        self.input_words = input_words
        function_to_call = getattr(self, "get_" + resource)
        function_to_call()

    def get_stack(self):
        # !bangs - !stackoverflow at start of request
        # gives multiple potential answers
        # choose for them first option - assume direct answer?
        # have option for search?
        # .class question-summary search-result are
        # so cssselect .question summary a ?

        # easy option -->
        self.link = "https://duckduckgo.com/?q=!stackoverflow " + self.input_words

    def get_ddg(self):
        # fallback
        self.link = "https://duckduckgo.com/?q=" + self.input_words

    def get_wiki(self):
        # !bangs - !wikipedia at start
        # gives direct document
        # even though link is search the term should give correct doc
        self.link = "https://duckduckgo.com/?q=!wikipedia " + self.input_words

    def get_docs(self):
        # !bangs - not python !java11 good test?
        # searches ddg pick top
        search_term = "!java11 " + (self.input_words.removesuffix('+java'))
        for s in search(search_term, max_results=1):
            self.link = s
        LOG.debug("search link", s)
        LOG.debug("link", self.link)


    def get_api(self):
        # search database
        # grab relevant doc
        self.link = " "

    # https://www.web-source.net/embedding_web_pages.htm
    # embed the resource in api webpage
