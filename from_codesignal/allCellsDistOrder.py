# Matrix Cells in Distance Order
# We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.
# Additionally, we are given a cell in that matrix with coordinates (r0, c0).
# Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  
# Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  
# (You may return the answer in any order that satisfies this condition.)

# Conditions
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C

# My code
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dis = []
        pair = []
        for i in range(R):
            for j in range(C):
                pair.append([i,j])
                dis.append(abs(r0-i)+abs(c0-j))
        
        id = sorted(range(len(dis)), key=lambda k: dis[k])
        ret = [pair[i] for i in id]
        
        return ret
        
       
