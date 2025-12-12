# Change


def find_fewest_coins(target, coins):
    if target < 0:
        raise ValueError("target can't be negative")
    if not isinstance(target, int):
        raise ValueError("can't make target with given coins")
    if target == 0:
        return []

    for amount in range(1, target +1):
        best: list[int] | None = None

        for coin in coins:
            if amount - coin >= 0 and dp[amount - coin] is not None:
                candidate = list[int] | None = dp[amount - coin] + [coin]
                if best is None or len(candidate) < len(best):
                    best = candidate

        dp[amount] = best

    if dp[target] is None:
        raise ValueError("can't make target with given coins")

    return sorted(dp[taget])
