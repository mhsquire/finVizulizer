from pytest_bdd import when, then, scenarios
from finVizulizer import request_wrapper as rw
from tests.helpers.config import finwiz_url

scenarios("../features/main.feature")


@when("a request for financial data is made")
def response_received(context):
    request_wrapper = rw.RequestWrapper()
    context["response"] = request_wrapper.get(url=finwiz_url + "TSLA")


@then("connection is ok")
def connection_is_ok(context):
    assert(context["response"].status_code == 200)
