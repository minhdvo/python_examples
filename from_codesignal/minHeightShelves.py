# Filling Bookcase Shelves
# We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].
# We want to place these books in order onto bookcase shelves that have total width shelf_width.
# We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width), then build another level 
# of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.  
# We repeat this process until there are no more books to place.
# Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  
# For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on 
# the second shelf, and the fourth and fifth book on the last shelf.
# Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

# conditions
# 1 <= books.length <= 1000
# 1 <= books[i][0] <= shelf_width <= 1000
# 1 <= books[i][1] <= 1000

# code
class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        n = len(books)
        f = [0] + [float('inf')]*n # f(i) := min height packinging books[:i]
        for i in xrange(n):
            w = h = 0
            j = i
            while j >= 0:
                w += books[j][0]
                h = max(h, books[j][1])
                if w > shelf_width: break
                f[i+1] = min(f[i+1], f[j] + h)
                j -= 1
        return f[-1]
