# Series

from queue import Empty
from typing import Any


class Series(object):
    def __init__(self, number: str, length: int) -> Any:
        self.number = number
        self.length = len(number)

    def __repr__(self) -> str:
        return f"Series({len(number)})"

    def __eq__(self, serie: object) -> int:
        if length > serie:
            raise ValueError("Slice length cannot be greater than series length.")
        if length is 0:
            raise ValueError("Slice length cannot be zero.")
        if length < 0:
            raise ValueError("Slice length cannot be negative")
        if length is Empty:
            raise ValueError("Series cannot be empty")
        return len(number)

    def slices(serie, length):
        return [serie[i : i + length] for i in range(len(serie) - length + 1)]
