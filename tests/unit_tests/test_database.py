import pytest

from finVizulizer.database import Database


@pytest.fixture
def database():
    return Database()


@pytest.fixture
def stock1():
    return {
        "name": "tesla",
        "ticker": "TSLA"
    }

@pytest.fixture
def stock2():
    return {
        "name": "tesla",
        "ticker": "TSLAHH"
    }

@pytest.fixture
def stocked_database(database, stock1):
    db = database
    database.stocks["TSLA"] = stock1
    return database


class TestDataBase:

    def test_init(self, database):
        assert database
        assert database.stocks == {}

    def test_insert(self, database, stock1):
        ticker = "TSLA"
        database.insert(ticker, stock1)
        assert database.stocks.get("TSLA")
        assert "tesla" in database.stocks["TSLA"]["name"]
        assert "TSLA" in database.stocks["TSLA"]["ticker"]

    def test_delete(self, stocked_database):
        ticker = "TSLA"
        stocked_database.delete(ticker)
        assert stocked_database.stocks == {}

    def test_read(self, stocked_database, stock1):
        ticker = "TSLA"
        assert stock1 == stocked_database.read(ticker)

    def test_update(self, stocked_database, stock1, stock2):
        ticker = "TSLA"
        stocked_database.update(ticker, stock2)
        assert stocked_database.stocks.get(ticker) == stock2