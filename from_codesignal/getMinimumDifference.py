# Minimum Absolute Difference in BST
# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
# Note: There are at least two nodes in this BST.

# code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        L = []
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(abs(a - b) for a, b in zip(L, L[1:]))
