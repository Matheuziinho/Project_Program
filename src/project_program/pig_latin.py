CONSONANTS = "bcdfghjklmnpqrstvwxz"
VOWELS = "aeiou"


def translate(word: str) -> str:
    # RULE 1:
    if word[0] in VOWELS or word.startswith(("xr", "yt")):
        return word + "ay"

    # RULE 3:
    if word.startswith(tuple(CONSONANTS)) and "qu" in word:
        position_qu = word.find("qu")
        return word[position_qu + 2 :] + word[: position_qu + 2] + "ay"

    # RULE 4:
    if word.startswith(tuple(CONSONANTS)) and "y" in word[1:]:
        position_y = word.find("y")
        return word[position_y:] + word[:position_y] + "ay"

    # RULE 2:
    for i, letter in enumerate(word):
        if letter in VOWELS:
            return word[i:] + word[:i] + "ay"

    return word + "ay"


# -----------------------------------------------------------------------
# My previous failed code
# -----------------------------------------------------------------------

# import re

# RULE1 = re.compile("[aeiou]+|xr|yt")
# RULE2 = re.compile("([bcdfghjklmnpqrstvwxyz]+)(.*)")
# RULE3 = re.compile("[bcdfghjklmnpqrstvwxyz]*qu(.*)")
# RULE4 = re.compile("([bcdfghjklmnpqrstvwxz]+)(y.*)")


# CONSONANTS = "bcdfghjklmnpqrstvwxz"
# VOWELS = "aeiou"

# def translate(word: str) -> str:
#    if RULE1.match(word):
#        return word + "ay"
#    elif RULE2.match(word):
#        if "xr" in word[:2] or "yt" in word[:2]:
#            return word + "ay"
#       elif "qu" in word[:2]:
#            return word[2:] + word[:2] + "ay"
#        elif word.startswith(tuple(CONSONANTS)):
#            for letter in word:
#                if letter in VOWELS:
#                    position = word.find(letter)
#                    return word[position:] + word[:position] + "ay"
#            return word[1:] + word[0] + "ay"
#    elif RULE3.match(word):
#        if word.startswith(tuple(CONSONANTS)) and "qu" in word:
#            position_qu = word.find("qu")
#            return word[position_qu + 2 :] + "qu" + "ay"
#    elif RULE4.match(word):
#        if word.startswith(tuple(CONSONANTS)) and "y" in word:
#            position_y = word.find("y")
#            return word[position_y + 1 :] + word[: position_y + 1] + "ay"
#        else:
#            return word[1:] + word[0] + "ay"
#    else:
#        return word + "ay"
#    return word + "ay"
