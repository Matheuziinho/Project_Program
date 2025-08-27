# Given a string containing brackets [], braces {}, parentheses (),
# or any combination thereof, verify that any and all pairs are matched
# and nested correctly. Any other characters should be ignored.


from inspect import stack


def is_paired(frase):
    brackets_open = {"(": ")", "[": "]", "{": "}"}
    brackets_close = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in frase:
        if char in brackets_open:
            stack.append(char)
        elif char in brackets_close:
            if not stack or stack[-1] != brackets_close[char]:
                return False
            stack.pop()

    return len(stack) == 0
