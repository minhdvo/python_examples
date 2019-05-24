# Longest String Chain
# Given a list of words, each word consists of English lowercase letters.
# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  
# For example, "abc" is a predecessor of "abac".
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a 
# predecessor of word_3, and so on.
# Return the longest possible length of a word chain with words chosen from the given list of words.

# Conditions
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters

# code
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        pool = [set() for _ in range(17)]
        for word in words:
            pool[len(word)].add(word)
        dp = {}
        for i in range(2, 17):
            for nxt in pool[i]:
                for j in range(i):
                    pre = nxt[:j] + nxt[j + 1:]
                    if pre in pool[i - 1]:
                        dp[nxt] = max(dp.get(nxt, 1), dp.get(pre, 1) + 1)
        ret = max(dp.values()) if dp else 1
        return ret
