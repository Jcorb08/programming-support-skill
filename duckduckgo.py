import requests
from lxml import html
import time
from mycroft.util.log import LOG


# https://github.com/thibauts/duckduckgo
# prints out list of urls
# edit to give descriptions too?
def search(keywords, max_results=None):
    url = 'https://duckduckgo.com/html/'
    params = {'q': keywords}
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    yielded = 0
    while True:
        res = requests.post(url, data=params, headers=headers)
        doc = html.fromstring(res.text)
        LOG.debug("res", res.text)

        results = [a.get('href') for a in doc.cssselect('#links .links_main a')]
        LOG.debug("results", len(results))
        for result in results:
            yield result
            time.sleep(0.1)
            yielded += 1
            if max_results and yielded >= max_results:
                return

        try:
            form = doc.cssselect('.results_links_more form')[-1]
        except IndexError:
            return
        params = dict(form.fields)
