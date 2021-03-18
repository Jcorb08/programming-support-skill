import webbrowser


class Output:
    def __init__(self, link):
        self.url = link
        self.output_url()

    def output_url(self):
        webbrowser.open(self.url, new=2, autoraise=True)
        # see if it can check if url is already open?
        # don't open if there
