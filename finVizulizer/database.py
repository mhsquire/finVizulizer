from setup_logger import logger
# stock schema:
#   name:
#   ticker:
#   date:
#   time:
#   headline:
#   article_link:
#   article_sentiment:


class Database:

    def __init__(self):
        self.stocks = {}
        logger.info("Database initialized.")

    def insert(self, ticker, info):
        self.stocks[ticker] = info
        logger.debug(f"Inserted {ticker}")

    def delete(self, ticker):
        self.stocks.pop(ticker)
        logger.debug(f"Deleted {ticker}")

    def read(self, ticker):
        logger.info(f"{ticker} read")
        return self.stocks.get(ticker)

    def update(self, ticker, new_info):
        self.stocks[ticker] = new_info
        logger.debug(f"Updated {ticker}")
