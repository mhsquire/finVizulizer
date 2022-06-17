from finVizulizer.database import Database


# Handles the storage of data for all tickers.

class DatabaseWrapper:

    db = None

    def __init__(self):
        # Initialize database
        if not self.db:
            self.db = Database()

    def put_ticker(self, ticker_name, data):
        self.db.insert(ticker_name, data)

    def remove_ticker(self, ticker_name):
        self.db.delete(ticker_name)

    def read_ticker(self, ticker_name):
        return self.db.read(ticker_name)

    def update_ticker(self, ticker, new_data):
        self.db.update(ticker, new_data)