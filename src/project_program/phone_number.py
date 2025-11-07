import re


def clean(number):
    return re.sub(r"[^0-9]", "", number)


class PhoneNumber(object):
    def __init__(self, number: str):
        number = clean(number)

        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(number) == 11:
            if number[0] != "1":
                raise ValueError("11 digits must start with 1")
            number = number[1:]

        if number[0] in "01":
            raise ValueError(
                "area code cannot start with zero"
                if number[0] == "0"
                else "area code cannot start with one"
            )

        if number[3] in "01":
            raise ValueError(
                "exchange code cannot start with zero"
                if number[3] == "0"
                else "exchange code cannot start with one"
            )

        if not number.isdigit():
            raise ValueError("punctuations not permitted")

        if not number.isalpha():
            raise ValueError("letters not permitted")

        self.number = number
        self.area_code = number[:3]
        self.exchange_code = number[3:6]
        self.subscriber_number = number[6:]

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
