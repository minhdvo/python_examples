# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, 
# the second - from the year 101 up to and including the year 200, etc.

# [input] integer year
# A positive integer, designating the year.

# Guaranteed constraints:
# 1 ≤ year ≤ 2005.

# [output] integer
# The number of the century the year is in.

def centuryFromYear(year):
    if (year % 100 )==0:
        x = year // 100
    else:
        x = year // 100 + 1
    return x
