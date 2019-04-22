# Given a binary tree t and an integer s, determine whether there is a root to leaf path in t 
# such that the sum of vertex values equals s.

# [input] tree.integer t
# A binary tree of integers.

# Guaranteed constraints:
# 0 ≤ tree size ≤ 5 · 104,
# -1000 ≤ node value ≤ 1000.

# [input] integer s
# An integer.

# Guaranteed constraints:
# -4000 ≤ s ≤ 4000.

# [output] boolean
# Return true if there is a path from root to leaf in t such that the sum of node values in it is equal to s, otherwise return false.
#
## Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if t is None:
        if s == 0:
            return 1
        else:
            return 0
    else:
        ans = 0
        subSum = s - t.value

        if subSum == 0 and t.left == None and t.right == None :
                return 1

        if t.left is not None:
            ans = ans or hasPathWithGivenSum(t.left, subSum)

        if t.right is not None:
            ans = ans or hasPathWithGivenSum(t.right, subSum)
        
        return ans    
