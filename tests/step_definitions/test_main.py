from pytest_bdd import scenario, given, when, then, scenarios

from conftest import context
from tests.helpers import config
from main import RequestWrapper

scenarios("../features/main.feature")



@when("a request for financial data is made")
def response_received(context):
    rw = RequestWrapper()
    context["response"] = rw.get(url=config.finwiz_url + "TSLA")


@then("connection is ok")
def connection_is_ok(context):
    assert(context["response"].status_code == 200)
