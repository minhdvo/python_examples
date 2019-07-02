''' All factors considered
Take a set of integers from STDIN and print to STDOUT a single integer that is the sum of all the integers
which have exactly three distinct factors excluding itself.
Input is a single line of integers that will contain only integers and not contain any letters, symbols or 
any newline characters. Each integer is separated by a comma.
Notes:
- the sum needs to be just of the integers from input array that meet the 3 factors criteria
- make sure the factors are distinct in nature
'''

# code
n = input()
n1 = n.split(',')
n2 = [int(i) for i in n1]
def find_no_factors(x):   
    n =0
    for i in range(1, x):
        if x % i == 0:
            n += 1
    return n
ret = 0
for j in n2:
    n = find_no_factors(j)
    if n==3:
        ret += j
print(ret)
