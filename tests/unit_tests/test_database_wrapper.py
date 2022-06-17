import pytest

from finVizulizer.database_wrapper import DatabaseWrapper


@pytest.fixture
def database_wrap():
    return DatabaseWrapper()


@pytest.fixture
def stock_data1():
    return {
        "name": "tesla",
        "ticker": "TSLA"
    }

@pytest.fixture
def stock_data2():
    return {
        "name": "tesla",
        "ticker": "TSLAHH"
    }

@pytest.fixture
def stocked_database(database_wrap, stock_data1):
    db = database_wrap
    db.db.stocks["TSLA"] = stock_data1
    return db


class TestDatabaseWrapper:

    def test_put_ticker(self, database_wrap, stock_data1):
        ticker = "TSLA"
        db = database_wrap
        db.put_ticker(ticker, stock_data1)
        assert db.db.read(ticker) == stock_data1

    def test_remove_ticker(self, stocked_database):
        ticker = "TSLA"
        db = stocked_database
        db.remove_ticker(ticker)
        assert db.db.read(ticker) == None

    def test_read_ticker(self, stocked_database, stock_data1):
        ticker = "TSLA"
        db = stocked_database
        assert stock_data1 == db.read_ticker(ticker)

    def test_update_ticker(self, stocked_database, stock_data2, stock_data1):
        ticker = "TSLA"
        db = stocked_database
        db.update_ticker(ticker, stock_data2)
        assert stock_data2 == db.db.read(ticker)