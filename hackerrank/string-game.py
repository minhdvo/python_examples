# String game
# Take a string from STDIN and print to STDOUT number of 'unique' words present in this string.
# Input will be a single line of text that can potentially contain letters, numbers, symbols and spaces, but will not
# contain any newline characters.
# Each word in the input is separated by a comma.
# - ignore any Cases
# - any non-alphanumerics should not be ingnored (i.e. Dr's and Drs should be considered as different strings)
# - look at unique string only

# code
import re
str = input()
str = str.lower()
str1 = str.split(',')
pattern = re.compile('\W')
str2 = []
for i in str1:
    if i.isalnum()==False:
        i = re.sub(pattern,'',i)
    str2.append(i)
res = set(str2)
print(len(res))
