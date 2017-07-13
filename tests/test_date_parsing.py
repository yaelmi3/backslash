import datetime
import functools
import pytest
from flask_app.search.value_parsers import parse_date
from flask_app.models import Session, Test


def test_exact_time(date_formatter, hour_formatter):
    min_time, max_time = parse_date(f'{date_formatter(2016, 1, 12)} {hour_formatter(23, 00, 20)}')

    assert min_time == max_time
    assert min_time == datetime.datetime(year=2016, month=1, day=12, hour=23, minute=0, second=20)


def test_non_exact_time(date_formatter):
    min_time, max_time = parse_date(f'{date_formatter(2016, 1, 12)}')

    assert max_time == min_time + datetime.timedelta(days=1)
    assert min_time == datetime.datetime(year=2016, month=1, day=12)



@pytest.fixture(params=['/', '-'])
def date_formatter(request):
    def formatter(*parts):
        return request.param.join(map(str, parts))
    return formatter

@pytest.fixture(params=[':'])
def hour_formatter(request):
    def formatter(*parts):
        return request.param.join(map(str, parts))
    return formatter
