# Adding Two Negabinary Numbers
# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.
# Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  
# For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array format is also 
# guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

# conditions
# 1 <= arr1.length <= 1000
# 1 <= arr2.length <= 1000
# arr1 and arr2 have no leading zeros
# arr1[i] is 0 or 1
# arr2[i] is 0 or 1

# code
class Solution:    
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 2000
        n1 = len(arr1)
        n2 = len(arr2)
        for i, x in enumerate(arr1):
            actual = n1 - i - 1
            if x: count[actual] += 1
        for i, x in enumerate(arr2):
            actual = n2 - i - 1
            if x: count[actual] += 1
        for i in range(1500):
            while count[i] > 1:
                if count[i + 1]:
                    count[i] -= 2
                    count[i + 1] -= 1
                else:
                    count[i] -= 2
                    count[i + 1] += 1
                    count[i + 2] += 1
        count.reverse()
        if 1 not in count: return [0]
        return count[count.index(1):]
    
    
