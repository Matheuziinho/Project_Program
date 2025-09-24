class ComplexNumber(object):
    def __init__(
        self,
        real: float,
        imaginary: float,
    ) -> None:
        self.real = real
        self.imaginary = imaginary

    def conjugate(
        self,
    ) -> "ComplexNumber":
        return ComplexNumber(self.real, -self.imaginary)

    def __abs__(
        self,
    ):  # -> Any:
        return (self.real**2 + self.imaginary**2) ** 0.5

    def __add__(
        self,
        other,
    ) -> "ComplexNumber":
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary,
        )

    def __sub__(
        self,
        other,
    ) -> "ComplexNumber":
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary,
        )

    def __mul__(
        self,
        other,
    ) -> "ComplexNumber":
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real,
        )

    def __truediv__(
        self,
        other,
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
            self.real / (self.real**2 + self.imaginary**2)
            - self.imaginary / (self.real**2 + self.imaginary**2)
        )
