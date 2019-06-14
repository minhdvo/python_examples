# Flip Columns For Maximum Number of Equal Rows
# Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  
# Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

# Return the maximum number of rows that have all values equal after some number of flips.

# condition
# 1 <= matrix.length <= 300
# 1 <= matrix[i].length <= 300
# All matrix[i].length's are equal
# matrix[i][j] is 0 or 1

# code
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        s = dict()
        for row in matrix:
            first = ''.join(map(str, row))
            second = ''.join(map(lambda x: str(1 - x), row))
            if first not in s: s[first] = 1
            else: s[first] += 1
            if second not in s: s[second] = 1
            else: s[second] += 1
        rtn = 0
        for key in s:
            rtn = max(rtn, s[key])
        return rtn
