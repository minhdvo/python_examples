# Greatest Common Divisor of Strings
# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)
# Return the largest string X such that X divides str1 and X divides str2.

# conditions
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.

# code
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        rtn = 0
        n1 = len(str1)
        n2 = len(str2)
        for i in range(1, min(n1, n2) + 1):
            if n1 % i == 0 and n2 % i == 0 and str1 == str1[:i] * (n1 // i) and str2 == str1[:i] * (n2 // i):
                rtn = i
        return str1[:rtn]
