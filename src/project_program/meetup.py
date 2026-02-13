import datetime

class MeetupDay:
    WEEKDAY = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    WEEK = {
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "last",
        "teenth",
    }
    MONTH = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    def __init__(self, year: int, month: int, weekday: str, week: str):
        self.year = year
        self.month = month
        self.weekday = weekday
        self.week = week

    def __repr__(self) -> str:
        return f"The({self.week}{self.weekday} of {self.month} {self.year})."

    # Verifies that weekday, week, and month values are valid, and raises ValueError if not.
    def validate(self) -> None:
        if self.weekday not in self.WEEKDAY:
            raise ValueError(f"Weekday '{self.weekday}' not recognized.")
        if self.week not in self.WEEK:
            raise ValueError(f"Week '{self.week}' not recognized.")
        if self.month not in self.MONTH:
            raise ValueError(f"Month '{self.month}' not recognized.")

    def meetup(self, year, month, weekday, week):
        self.validate()
        # Get the first day of the month
        first_day = datetime.date(year, month, 1)
        # Find the first occurrence of the specified weekday in the month
        first_weekday = first_day + datetime.timedelta(days=(self.WEEKDAY.index(weekday) - first_day.weekday()) % 7)
        if week == "first":
            return first_weekday
        elif week == "second":
            return first_weekday + datetime.timedelta(days=7)
        elif week == "third":
            return first_weekday + datetime.timedelta(days=14)
        elif week == "fourth":
            return first_weekday + datetime.timedelta(days=21)
        elif week == "fifth":
            return first_weekday + datetime.timedelta(days=28)
        elif week == "last":
            last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
            last_weekday = last_day - datetime.timedelta(days=(last_day.weekday() - self.WEEKDAY.index(weekday)) % 7)
            return last_weekday
        elif week == "teenth":
            teenth_day = datetime.date(year, month, 13)
            teenth_weekday = teenth_day + datetime.timedelta(days=(self.WEEKDAY.index(weekday) - teenth_day.weekday()) % 7)
            return teenth_weekday
        else:
            raise ValueError("That day doesn't exist.")
