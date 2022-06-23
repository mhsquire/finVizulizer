import re

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
    return 200, open("tests/helpers/finviz_page.html").read()


@when("the response is parsed", target_fixture="news")
def the_response_is_parsed(response):
    _, html = response
    parsed_html = pt.read_html(html)
    news = pt.find_news(parsed_html)
    return pt.parse_news(news)


@then("the resulting table records date")
def the_resulting_table_records_date(news):
    # matches 3 letters (-) 2 numbers (-) 2 numbers
    date = re.compile("^\w{3}-\d{2}-\d{2}")
    for article in news:
        comma_article = article.split(",")
        print(comma_article[0])
        assert date.match(comma_article[0])


@then("the resulting table records time")
def step_impl():
    raise NotImplementedError(u'STEP: And the resulting table records time')


@then("the resulting table records headline")
def step_impl():
    raise NotImplementedError(u'STEP: And the resulting table records headline')


@then("the resuting table records article link")
def step_impl():
    raise NotImplementedError(u'STEP: And the resuting table records article link')