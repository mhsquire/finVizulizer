import requests


class RequestWrapper:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

    def get(self, url):

        return requests.get(url, headers=self.headers)


if __name__ == "__main__":
    pass


# finwiz_url = 'https://finviz.com/quote.ashx?t='news_tables = {}
# tickers = ['AMZN', 'TSLA', 'GOOG']for ticker in tickers:
#     url = finwiz_url + ticker
#     req = Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
#     response = urlopen(req)
#     # Read the contents of the file into 'html'
#     html = BeautifulSoup(response)
#     # Find 'news-table' in the Soup and load it into 'news_table'
#     news_table = html.find(id='news-table')
#     # Add the table to our dictionary
#     news_tables[ticker] = news_table
