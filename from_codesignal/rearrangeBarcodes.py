# Distant Barcodes
# In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

# Conditions
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000

# code
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        n = len(barcodes)
        idxes = collections.deque(list(range(0, n, 2)) + list(range(1, n, 2)))
        counter = collections.Counter(barcodes)
        ans = [None] * n
        for num, cnt in counter.most_common():
            for _ in range(cnt):
                ans[idxes.popleft()] = num
        return ans
