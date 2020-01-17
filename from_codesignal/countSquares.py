# Count Square Submatrices with All Ones
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
# Constraints:
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])
        p = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                p[i+1][j+1] = p[i+1][j] + p[i][j+1] - p[i][j] + matrix[i][j]
        def a(i, j, k):
            return p[i][j] + p[i-k][j-k] - p[i-k][j] - p[i][j-k] == k*k
        def f(i, j):
            if matrix[i-1][j-1] == 0: return 0
            x, y = 1, min(i, j)+1
            while x+1 < y:
                z = (x+y) >> 1
                if a(i, j, z): x=z
                else: y=z
            return x
        return sum(f(i+1, j+1) for i in range(n) for j in range(m))
