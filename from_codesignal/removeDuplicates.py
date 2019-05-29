# Remove All Adjacent Duplicates In String
# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
# We repeatedly make duplicate removals on S until we no longer can.
# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

# conditions
# 1 <= S.length <= 20000
# S consists only of English lowercase letters.

# Codes
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for ch, gp in itertools.groupby(S):
            if len(list(gp)) & 1:
                if stack and stack[-1] == ch:
                    stack.pop()
                else:
                    stack.append(ch)
        return ''.join(stack)
