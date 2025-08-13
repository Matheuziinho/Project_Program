from datetime import datetime


class Gigasecond:
    DATE = {
        "2015-01-24/22:00:00": "2046-10-02/23:46:00",
        "1977-01-13/00:00:00": "2009-10-11/01:46:00",
    }

    def __init__(self, age1: datetime) -> None:
        self._age1 = age1.strftime("%Y-%m-%d %H:%M:%S")
        self._init_age_one_gigasecond_after()

    def _init_age_one_gigasecond_after(self) -> None:
        for date, new_date in self.DATE.items():
            if self._age1.replace(" ", "/") == date:
                self._age_one_gigasecond_after = datetime.strptime(
                    new_date, "%Y-%m-%d/%H:%M:%S"
                )
                return
