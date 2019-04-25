# Sum of Even Numbers After Queries

# We have an array A of integers, and an array queries of queries.
# For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  
# Then, the answer to the i-th query is the sum of the even values of A.
# (Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

# Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

# Condition
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# 1 <= queries.length <= 10000
# -10000 <= queries[i][0] <= 10000
# 0 <= queries[i][1] < A.length

# Code
class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        n = len(A)
        B = [(1-A[i]%2)*A[i] for i in range(n)]            
        x = sum(B)    
        
        for query in queries:            
            val = query[0]
            ind = query[1]                        
            
            x1 = A[ind] %2
            x2 = val %2
            

            if (x1==0 and x2==0): # even even
                x = x + val
            elif (x1==1 and x2==1): #odd odd
                x = x + A[ind]+val                
            elif (x1==0 and x2==1): #even odd
                x = x - A[ind]
            
            A[ind]=A[ind]+val
            ret.append(x)
        
        return ret
