from string import ascii_uppercase


def rows(letter: str) -> list[str]:
    length = ascii_uppercase.index(letter)
    stack: list[str] = []

    # Superior line
    for i in range(length + 1):
        char = ascii_uppercase[i]
        side_points = "." * (length - i)
        center_points = "." * (2 * i - 1)

        if not i:
            stack.append(f"{side_points}{char}{side_points}")
        else:
            # Center lines
            stack.append(f"{side_points}{char}{center_points}{char}{side_points}")

    # Inferior line
    stack.extend(stack[:-1][::-1])

    return stack
