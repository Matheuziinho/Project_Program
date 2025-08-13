from datetime import datetime

from project_program.gigasecond import gigasecond


def test_gigasecond() -> None:
    assert gigasecond(datetime(2015, 1, 24, 22, 0)) == datetime(2046, 10, 2, 23, 46)
    assert gigasecond(datetime(1977, 1, 13)) == datetime(2009, 10, 11, 1, 46)
