# Last Stone Weight
# We have a collection of rocks, each rock has a positive integer weight.
# Each turn, we choose the two heaviest rocks and smash them together.  
# Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Conditions
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

# codes
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, -(a - b))
        return -stones[0] if stones else 0
