# Find the thirteen adjacent digits in the digit number that have the greatest product. What is the value of this product?


def largest_product(number: str, length: int) -> int:
    max_product = 0

    for i in range(len(number) - length + 1):
        product = 1

        for j in range(length):
            product *= int(number[i + j])

        if product > max_product:
            max_product = product

    return max_product
