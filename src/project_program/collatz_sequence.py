def collatz(starting_number: int) -> int:
    length = 0
    while starting_number > 1:
        length += 1

        if starting_number % 2 == 0:
            starting_number = starting_number // 2

        else:
            starting_number = 3 * starting_number + 1
            if starting_number == 1:
                length += 1
                break
    return length, starting_number


def biggest_sequence(limit: int) -> int:
    return max(collatz(i) for i in range(1, limit))
