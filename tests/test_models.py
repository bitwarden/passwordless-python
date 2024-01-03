import time
from datetime import datetime, timedelta, timezone

from dateutil import parser

from tests.data_factory import (
    build_register_token,
    build_register_token_without_expires_at,
)


def test_new_register_token_expires_at_provided() -> None:
    register_token = build_register_token()
    assert register_token.expires_at == parser.parse(
        "2023-09-09T20:07:02.365573Z"
    )


def test_new_register_token_expires_at_default() -> None:
    time_now = datetime.now(timezone.utc).replace(tzinfo=None)
    register_token = build_register_token_without_expires_at()
    diff = register_token.expires_at - time_now
    assert diff.total_seconds() > 0
    assert diff < timedelta(minutes=3)
    assert diff >= timedelta(minutes=2)


def test_new_register_token_expires_at_default_sleep() -> None:
    register_token_1 = build_register_token_without_expires_at()
    time.sleep(0.1)
    register_token_2 = build_register_token_without_expires_at()
    assert register_token_1.expires_at != register_token_2.expires_at
    diff = register_token_2.expires_at - register_token_1.expires_at
    assert diff.total_seconds() > 0
    assert diff < timedelta(seconds=10)
