import re


def clean(number):
    return re.sub(r"[^0-9]", "", number)


class PhoneNumber(object):
    def __init__(self, number: str):
        clean_number = (
            number.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        )

        if len(clean_number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(clean_number) > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(clean_number) == 11:
            if clean_number[0] != "1":
                raise ValueError("11 digits must start with 1")
            clean_number = clean_number[1:]

        if clean_number[0] in "01":
            raise ValueError(
                "area code cannot start with zero"
                if clean_number[0] == "0"
                else "area code cannot start with one"
            )

        if clean_number[3] in "01":
            raise ValueError(
                "exchange code cannot start with zero"
                if clean_number[3] == "0"
                else "exchange code cannot start with one"
            )

        if not clean_number.isdigit():
            raise ValueError("punctuations not permitted")

        if clean_number.isalpha():
            raise ValueError("letters not permitted")

        self.number = clean_number
        self.area_code = clean_number[:3]
        self.exchange_code = clean_number[3:6]
        self.subscriber_number = clean_number[6:]

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
