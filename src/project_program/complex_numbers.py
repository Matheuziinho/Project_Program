import math


class ComplexNumber(object):
    def __init__(
        self,
        real: float,
        imaginary: float,
    ) -> None:
        self.real = real
        self.imaginary = imaginary

    def __repr__(self) -> str:
        return f"ComplexNumber({self.real}, {self.imaginary}i)"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ComplexNumber):  # If other is NOT a ComplexNumber
            return False  # Return False (can't be equal)
        return self.real == other.real and self.imaginary == other.imaginary

    def conjugate(
        self,
    ) -> "ComplexNumber":
        return ComplexNumber(self.real, -self.imaginary)

    def __abs__(
        self,
    ) -> float:
        return math.sqrt(self.real**2 + self.imaginary**2)

    def __add__(
        self,
        other: "ComplexNumber",
    ) -> "ComplexNumber":
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary,
        )

    def __sub__(
        self,
        other: "ComplexNumber",
    ) -> "ComplexNumber":
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary,
        )

    def __mul__(
        self,
        other: "ComplexNumber",
    ) -> "ComplexNumber":
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real,
        )

    def __truediv__(
        self,
        other: "ComplexNumber",
    ) -> "ComplexNumber":
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary)
            / (other.real**2 + other.imaginary**2),
            (self.imaginary * other.real - self.real * other.imaginary)
            / (other.real**2 + other.imaginary**2),
        )

    def reciprocal(
        self,
    ) -> "ComplexNumber":
        return ComplexNumber(
            self.real / (self.real**2 + self.imaginary**2),
            -self.imaginary / (self.real**2 + self.imaginary**2),
        )

    def exponential(
        self,
        e_value: float = math.e,
    ) -> "ComplexNumber":
        return ComplexNumber(
            e_value**self.real * math.cos(self.imaginary),
            e_value**self.real * math.sin(self.imaginary),
        )
