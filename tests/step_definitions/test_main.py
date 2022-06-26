import re
import csv

from pytest_bdd import given, when, then, scenarios
from finVizulizer import request_wrapper as rw
from finVizulizer.parse_table import ParseTable as pt
from tests.helpers.config import finwiz_url


scenarios("../features/main.feature")


@when("a request for financial data is made")
def response_received(context):
    request_wrapper = rw.RequestWrapper()
    context["response"] = request_wrapper.get(url=finwiz_url + "TSLA")


@then("connection is ok")
def connection_is_ok(context):
    assert(context["response"].status_code == 200)


@given("a response has been sent", target_fixture="response")
def a_response_has_been_sent():
    with open("tests/helpers/finviz_page.html", 'r') as file:
        return file.read()


@when("the response is parsed", target_fixture="news")
def the_response_is_parsed(response):
    parsed_html = pt.read_html(response)
    news = pt.find_news(parsed_html)
    return pt.parse_news(news)


@then("the resulting table records date")
def the_resulting_table_records_date(news):
    # matches 3 letters (-) 2 numbers (-) 2 numbers
    date = re.compile("^\w{3}-\d{2}-\d{2}")
    count = 0
    for article in news:
       count = count + 1
       assert date.match(article[0]), f"Failed at article {count}"


@then("the resulting table records time")
def the_resulting_table_records_time(news):
    # time is 2 digits : 2 digits then AM or 2 digits : 2 digits then PM
    time = re.compile("^\d{2}:\d{2}AM|^\d{2}:\d{2}PM")
    count = 0
    for article in news:
        count = count + 1
        assert(time.match(article[1]), f"Failed at article {count}")



@then("the resulting table records the headline")
def the_resulting_table_records_the_headline(news):
    for article in news:
        assert type(article[2]) == str



@then("the resulting table records article link")
def the_resulting_table_records_article_link(news):
    link = re.compile("[-a-zA-Z0-9@:%._+~#=]{1,256}")
    count = 0
    for article in news:
        count = count + 1
        assert link.match(article[3]), f"Failed at article {count}"
