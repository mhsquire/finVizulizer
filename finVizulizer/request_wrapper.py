import requests


# Handles the logistics of requesting data for a ticker.

class RequestWrapper:

    def __init__(self, headers=None):
        if not headers:
            self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

    def get(self, url):
        return requests.get(url, headers=self.headers)
