# Last Stone Weight II
# We have a collection of rocks, each rock has a positive integer weight.
# Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  
# The result of this smash is:
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone 
# (the weight is 0 if there are no stones left.)

# conditions
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100

# code
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        ret = {0}
        for x in stones:
            temp = set()
            for item in ret:
                temp.add(item - x)
                temp.add(item + x)
            ret = temp
        return min(ret, key=abs)
