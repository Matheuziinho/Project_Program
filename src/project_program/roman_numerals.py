def transformation(
    arabic: int,
) -> str:
    roman_values = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    result = ""

    for value in roman_values.keys():
        while arabic >= value:
            result += roman_values[value]
            arabic -= value

    return result
