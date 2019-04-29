# Moving Stones Until Consecutive
# Three stones are on a number line at positions a, b, and c.
# Each turn, let's say the stones are currently at positions x, y, z with x < y < z.  You pick up the stone at either position x or 
# position z, and move that stone to an integer position k, with x < k < z and k != y.
# The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.
# When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: 
# answer = [minimum_moves, maximum_moves]

# Conditions
# 1 <= a <= 100
# 1 <= b <= 100
# 1 <= c <= 100
# a != b, b != c, c != a

# code
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:        
        x, y, z = sorted((a, b, c))
        max_move = z - x - 2
        if max_move == 0:
            min_move = 0
        # 1 2 10 or 1 3 5
        elif (x + 1 == y or y + 1 == z) or (x + 2 == y or y + 2 == z):
            min_move = 1
        else:
            min_move = 2
        return [min_move, max_move]

            
