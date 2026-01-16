# Counting Sundays

from datetime import date


def counting(y1: int, y2: int):
    count = 0
    for year in range(y1, y2 + 1):
        for month in range(1, 13):
            d = date(year, month, 1)
            if d.weekday() == 6:
                count += 1
    return count
