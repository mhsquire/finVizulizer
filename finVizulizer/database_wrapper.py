from finVizulizer.database import Database

from finVizulizer.setup_logger import logger
# Handles the storage of data for all tickers.


class DatabaseWrapper:

    db = None

    def __init__(self):
        # Initialize database
        if not self.db:
            logger.debug("Creating database.")
            self.db = Database()

    def put_ticker(self, ticker_name, data):
        self.db.insert(ticker_name, data)
        logger.debug(f"Insert {ticker_name}")

    def remove_ticker(self, ticker_name):
        self.db.delete(ticker_name)
        logger.debug(f"Deleted {ticker_name}")

    def read_ticker(self, ticker_name):
        info = self.db.read(ticker_name)
        logger.debug(f"Read {ticker_name}")
        return info

    def update_ticker(self, ticker_name, new_data):
        self.db.update(ticker_name, new_data)
        logger.debug(f"Updated {ticker_name}")