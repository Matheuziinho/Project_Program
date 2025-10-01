import math


class RationalNumber(object):
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.rational = numerator / denominator

    def __repr__(self) -> str:
        return f"RationalNumber({self.numerator}/{self.denominator})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RationalNumber):
            return False
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __add__(self, other: "RationalNumber") -> "RationalNumber":
        return RationalNumber(
            self.numerator * other.denominator
            + other.numerator * self.denominator,  # numerator
            self.denominator * other.denominator,  # denominator
        )

    def __sub__(self, other: "RationalNumber") -> "RationalNumber":
        return RationalNumber(
            self.numerator * other.denominator
            - other.numerator * self.denominator,  # numerator
            self.denominator * other.denominator,  # denominator
        )

    def __mul__(self, other: "RationalNumber") -> "RationalNumber":
        return RationalNumber(
            self.numerator * other.numerator,  # numerator
            self.denominator * other.denominator,  # denominator
        )

    def __truediv__(self, other: "RationalNumber") -> "RationalNumber":
        return RationalNumber(
            self.numerator * other.denominator,  # numerator
            self.denominator * other.numerator,  # denominator
        )

    def __abs__(self) -> "RationalNumber":
        return RationalNumber(abs(self.numerator), abs(self.denominator))

    def __pow__(self, power):
        if isinstance(power, int) and power >= 0:
            return RationalNumber(self.numerator**power, self.denominator**power)
        elif isinstance(power, int) and power < 0:
            return RationalNumber(
                self.denominator ** abs(power), self.numerator ** abs(power)
            )
        else:
            return self.numerator**power / self.denominator**power

    def __rpow__(self, base):
        if not isinstance(base, (int, float)):
            raise ValueError("Base must be a number.")
        return base ** (self.numerator / self.denominator)
