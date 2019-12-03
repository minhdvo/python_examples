# Find Winner on a Tic Tac Toe Game
# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

# Here are the rules of Tic-Tac-Toe:

# - Players take turns placing characters into empty squares (" ").
# - The first player A always places "X" characters, while the second player B always places "O" characters.
# - "X" and "O" characters are always placed into empty squares, never on filled ones.
# - The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# - The game also ends if all squares are non-empty.
# - No more moves can be played if the game is over.
# Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark 
# their respective character in the order in which A and B play.

# Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to 
# play return "Pending".

# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

class Solution(object):
    def tictactoe(self, moves):
        grid = ["   ", "   ", "   "]
        def f(c):
            if c == 'X': return "A"
            return "B"
        def status(grid):
            for i in range(3):
                if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2] and grid[i][2] != ' ':
                    return f(grid[i][0])
                if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i] and grid[0][i] != ' ':
                    return f(grid[0][i])
            if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[1][1] != ' ':
                return f(grid[0][0])
            if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[1][1] != ' ':
                return f(grid[0][2])
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == ' ': return "Pending"
            return "Draw"
        for i in range(len(moves)):
            x = 'X'
            if i % 2 == 1: x = 'O'
            X, Y = moves[i]
            grid[X] = grid[X][:Y] + x + grid[X][Y+1:]
        return status(grid)
