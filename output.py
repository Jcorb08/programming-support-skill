import webbrowser


class Output:
    def __init__(self, link):
        self.url = link

    def output_url(self):
        webbrowser.open(self.url, new=2, autoraise=True)
        # needs more?
