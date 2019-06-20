# Grumpy Bookstore Owner
# Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) 
# enter the store, and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise 
# grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

# The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.

# conditions
# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1

# code
class Solution(object):
    # def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        ncus = 0
        nbad = 0
        n = len(customers)
        for i in range(n):
            ncus += customers[i]
            if grumpy[i]:
                nbad += customers[i]
            else:
                customers[i] = 0
        best = cur = 0
        for i in range(n):
            cur += customers[i]
            if i >= X:
                cur -= customers[i - X]
            best = max(cur, best)
        return ncus - (nbad - best)
