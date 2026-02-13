#Names Scores

import pandas as pd
df = pd.read_csv('names.txt')

def scores():
    return sum(index * sum(ord(letter) - 64 for letter in name)
        for index, name in enumerate(sorted(self.names), start=1))
