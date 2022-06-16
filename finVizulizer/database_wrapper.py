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
