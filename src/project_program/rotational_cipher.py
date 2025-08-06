# Rotational cipher

chars = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text, key):
    newchars = chars[key:] + chars[:key]  # Criamos uma nova string com os caracteres rotacionados
    trans = str.maketrans(chars, newchars)
    return text.translate(trans)

