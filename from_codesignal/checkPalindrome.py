# Given the string, check if it is a palindrome.

# [input] string inputString
# A non-empty string consisting of lowercase characters.

# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 105.

# [output] boolean
# true if inputString is a palindrome, false otherwise.

def checkPalindrome(inputString):
    rev = reserve_string(inputString)
    
    if rev == inputString:
        ret = True
    else:
        ret = False
    
    return ret
            
def reserve_string(inputString):
    return inputString[::-1]
