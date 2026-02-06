# Counting every Sunday between years y1 and y2

from datetime import date


def counting(y1: int, y2: int) -> int:
    count = 0
    for year in range(y1, y2 + 1):
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    d = date(year, month, day)
                except ValueError:
                    continue
                if d.weekday() == 6:
                    count += 1
    return count


# Counting the first day of each month that is a Sunday
# def counting(y1: int, y2: int) -> int:
#    count = 0
#    for year in range(y1, y2 + 1):
#        for month in range(1, 13):
#            d = date(year, month, 1)
#            if d.weekday() == 6:
#                count += 1
#    return count
