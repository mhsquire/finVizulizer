import pytest

from finVizulizer.database_wrapper import DatabaseWrapper


@pytest.fixture
def database_wrap():
    return DatabaseWrapper()


@pytest.fixture
def stock1_data():
    return {
        "name": "tesla",
        "ticker": "TSLA"
    }


class TestDatabaseWrapper:

    def test_put_ticker(self, database_wrap, stock1_data):
        ticker = "TSLA"
        db = database_wrap
        db.put_ticker(ticker, stock1_data)
        assert db.db.read(ticker) == stock1_data
