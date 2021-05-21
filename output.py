import webbrowser


# create a new object Output
class Output:
    def __init__(self, link):
        # set url to the link url from resource class
        self.url = link
        # output url to user
        self.output_url()

    def output_url(self):
        # opens a new tab in the webbrowser that has the url set before
        webbrowser.open(self.url, new=2, autoraise=True)

