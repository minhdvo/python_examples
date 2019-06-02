# Number of Submatrices That Sum to Target
# Given a matrix, and a target, return the number of non-empty submatrices that sum to target.
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that 
# is different: for example, if x1 != x1'.

# Conditions
# 1 <= matrix.length <= 300
# 1 <= matrix[0].length <= 300
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8

# code
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            for i in range(m):
                if i == 0: dp[i][j] = matrix[0][j]
                else: dp[i][j] = dp[i - 1][j] + matrix[i][j]
        rtn = 0       
        for r1 in range(m):
            for r2 in range(r1, m):
                # A[r1...r2][c...d] = target
                index = {0: 1}
                curr = 0
                for c in range(n):
                    curr += dp[r2][c]
                    if r1: curr -= dp[r1 - 1][c]
                    if curr - target in index:
                        rtn += index[curr - target]
                    if curr not in index: index[curr] = 1
                    else: index[curr] += 1
        return rtn
