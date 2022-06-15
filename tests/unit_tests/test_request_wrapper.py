import pytest

from finVizulizer.request_wrapper import RequestWrapper


class TestRequestWrapper:

    def test_init_no_headers(self):
        rw = RequestWrapper()
        assert rw.headers, "No headers detected, did something clobber the default headers in init?"

    def test_get(self):
        rw = RequestWrapper()
        rw.get("https://www.google.com")
