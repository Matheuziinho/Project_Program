# Counting Sundays

from datetime import date


def counting(count):
   for year in range(1900, 2001):
        for month in range(1, 13):
            d = date(year, month, 1)
            if d.weekday() == 6:
                count += 1
    return count
