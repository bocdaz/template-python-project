import logging

import pytest
import requests
from _pytest.logging import caplog as _caplog  # noqa: F401
from loguru import logger


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())


@pytest.fixture
def caplog(_caplog):  # noqa: F811
    class PropogateHandler(logging.Handler):
        """Propagate logs to pytest's `caplog`.

        This is only necessary if you want to make an assertion inside of a
        test of what is being logged using the pytest `caplog`.

        See:
        - https://docs.pytest.org/en/latest/how-to/logging.html#caplog-fixture
        - https://github.com/Delgan/loguru/issues/59
        """

        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    handler_id = logger.add(PropogateHandler(), format="{message} {extra}")
    yield _caplog
    logger.remove(handler_id)
