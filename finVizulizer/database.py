

# stock schema:
#       name:
#       ticker:


class Database:

    def __init__(self):
        self.stocks = {}

    def insert(self, ticker, info):
        self.stocks[ticker] = info

    def delete(self, ticker):
        self.stocks.pop(ticker)

    def read(self, ticker):
        return self.stocks.get(ticker)

    def update(self, ticker, new_info):
        self.stocks[ticker] = new_info
