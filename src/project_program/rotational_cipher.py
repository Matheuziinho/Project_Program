# Rotational cipher

chars = "abcdefghijklmnopqrstuvwxyz"


def rotate_chars(text, key):
    chars_lower = chars[key:] + chars[:key]
    chars_upper = chars.upper()[key:] + chars.upper()[:key]
    trans = str.maketrans(chars + chars.upper(), chars_lower + chars_upper)
    return text.translate(trans)
