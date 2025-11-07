# Series


class Series(object):
    def __init__(self, number: str):
        self.number = number
        self.length = len(number)

    def __repr__(self) -> str:
        return f"Series({self.length})"

    def slices(self, length: int):
        if not self.number:
            raise ValueError("Series cannot be empty.")
        if length > self.length:
            raise ValueError("Slice length cannot be greater than series length.")
        if not length:
            raise ValueError("Slice length cannot be zero.")
        if length < 0:
            raise ValueError("Slice length cannot be negative.")
        return [self.number[i : i + length] for i in range(self.length - length + 1)]
