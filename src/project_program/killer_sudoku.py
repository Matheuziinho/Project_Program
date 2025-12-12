import itertools


def combinations(target, size, exclude):
    candidates = [
        number for number in range(1, min(target, 9) + 1) if number not in exclude
    ]

    for combo in itertools.combinations(candidates, size):
        if sum(combo) == target:
            yield combo
