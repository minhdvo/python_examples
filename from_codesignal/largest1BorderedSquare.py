""" Largest 1-Bordered Square
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a 
subgrid doesn't exist in the grid.

Constraints:
1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1

Code """
class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """       
        ret = -1
        n, m = len(grid), len(grid[0])
        l, r, u, d = [[[0] * m for i in range(n)] for j in range(4)]
        for i in range(n):
            for j in range(m):
                u[i][j] = 0 if grid[i][j] == 0 else u[i - 1][j] + 1 if i >= 1 else 1
                l[i][j] = 0 if grid[i][j] == 0 else l[i][j - 1] + 1 if j >= 1 else 1
                
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                d[i][j] = 0 if grid[i][j] == 0 else d[i + 1][j] + 1 if i < n - 1 else 1
                r[i][j] = 0 if grid[i][j] == 0 else r[i][j + 1] + 1 if j < m - 1 else 1
                
        for i in range(n):
            for j in range(m):
                p = min(d[i][j], r[i][j])
                for k in range(p - 1, -1, -1):
                    if k <= ret:
                        break
                    if min(u[i + k][j + k], l[i + k][j + k]) >= k:
                        ret = max(ret, k)
        return (ret + 1) ** 2
