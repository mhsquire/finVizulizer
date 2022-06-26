import csv
import json
import tempfile

import pytest
from bs4 import BeautifulSoup

from finVizulizer.parse_table import ParseTable as pt


@pytest.fixture
def response():
    html = open("tests/helpers/finviz_page.html").read()
    response_code = 200
    return response_code, html


@pytest.fixture
def parsed_table():
    parsed = open("tests/helpers/finviz_table.html").read()
    return BeautifulSoup(parsed, "html.parser")

@pytest.fixture
def html_response(response):
    response_code, html = response
    return BeautifulSoup(html, "html.parser")

@pytest.fixture
def example_table():
    example = f'Jun-19-22,09:53AM,Dow Jones Futures: What To Do As Bear Market Intensifies; Bitcoin Bounces From Below $18\,000,https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-what-to-do-as-bear-market-intensifies-tesla-rival-leads-5-key-stocks/?src=A00220'
    return example


class TestParseTable:

    def test_read_html(self, response):
        response_code, html = response
        bs_html = pt.read_html(response=html)
        assert type(bs_html) == BeautifulSoup

    def test_find_news(self, html_response, parsed_table):
        news = pt.find_news(parsed_response=html_response)
        compare = pt.find_news(parsed_response=parsed_table)
        assert news == compare

    def test_parse_news(self, example_table, parsed_table):
        json_object = pt.parse_news(parsed_table)
        print(json_object)

        example_csv = "tests/helpers/parsenews.json"
        with open(example_csv, "r") as f:
            freader = json.loads(f.read())
            print (freader)
            assert freader == json_object

