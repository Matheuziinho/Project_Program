def get_divisors(n: int) -> list[int]:
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if not n % i:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)


class AmicableNumbers:
    def __init__(self, number: int) -> None:
        self.number = number

    def __repr__(self) -> str:
        return f"AmicableNumbers({self.number})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AmicableNumbers):
            return False
        return self.number == other.number

    def divisors(self) -> list[int]:
        return get_divisors(self.number)

    def sum_of_divisors(self) -> int:
        return sum(self.divisors()) - self.number

    def is_amicable(self, other: object) -> bool:
        if not isinstance(other, AmicableNumbers):
            return False
        return (
            self.sum_of_divisors() == other.number
            and other.sum_of_divisors() == self.number
        )


def counting_amicable_pairs(limit: int) -> int:
    amicable_pairs = set()
    for num in range(2, limit):
        current = AmicableNumbers(num)
        partner_num = current.sum_of_divisors()
        if partner_num != num:
            partner = AmicableNumbers(partner_num)
            if current.is_amicable(partner):
                pair = tuple(sorted((num, partner_num)))
                amicable_pairs.add(pair)
    return len(amicable_pairs)
