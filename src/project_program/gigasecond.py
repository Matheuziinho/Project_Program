from datetime import date, datetime, timedelta


class Gigasecond:
    def __init__(self, moment):
        self.moment = moment

    def one_gigasecond(datetime):
        return datetime + timedelta(seconds=10**9)

    def date(self):
        return Gigasecond.one_gigasecond(self.moment)
