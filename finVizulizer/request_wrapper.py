import requests
from finVizulizer.setup_logger import logger


class RequestWrapper:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
        logger.debug(f"request_wrapper initialized.")

    def get(self, url):
        response = requests.get(url, headers=self.headers)
        logger.debug(f"Response from {url} is {response.status_code}")
        return response
