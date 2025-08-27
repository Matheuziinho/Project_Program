from datetime import datetime

from project_program.gigasecond import Gigasecond


def test_add_a_gigasecond_to_a_date():
    gs = Gigasecond(datetime(2015, 1, 24, 22, 0))
    assert gs.date() == datetime(2046, 10, 2, 23, 46, 40)
