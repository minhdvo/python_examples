# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# [input] array.integer inputArray
# An array of integers containing at least two elements.

# Guaranteed constraints:
# 2 ≤ inputArray.length ≤ 10,
# -1000 ≤ inputArray[i] ≤ 1000.

# [output] integer
# The largest product of adjacent elements.

def adjacentElementsProduct(inputArray):
    a = inputArray[:-1]
    b = inputArray[1:]
    c = [i*j for i,j in zip(a,b)]
    return max(c)
