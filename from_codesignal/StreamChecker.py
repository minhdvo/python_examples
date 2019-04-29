# Stream of Characters
# Implement the StreamChecker class as follows:
# StreamChecker(words): Constructor, init the data structure with the given words.
# query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, 
# including this letter just queried) spell one of the words in the given list.

# Conditions
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 2000
# Words will only consist of lowercase English letters.
# Queries will only consist of lowercase English letters.
# The number of queries is at most 40000.

# code
class Trie(object):
    def __init__(self, words):
        self.data = [None] * 27
        for word in words:
            layer = self.data
            for char in word:
                index = ord(char) - ord('a')
                if layer[index] is None:
                    layer[index] = [None] * 27
                layer = layer[index]
            layer[-1] = True


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie(words)
        self.poss = [self.trie.data]

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        nposs = list()
        index = ord(letter) - ord('a')
        ans = False
        for poss in self.poss:
            if poss[index] is not None:
                if poss[index][-1]:
                    ans = True
                nposs.append(poss[index])
        nposs.append(self.trie.data)
        self.poss = nposs
        return ans


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
