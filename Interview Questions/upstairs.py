#TCO(2^n)
# In how many ways a person can reach upstairs(n) if:
#   1. he can go one or two steps at a time

'''
let's say we have n = 0 ---> way = 0
n = 1 ---> ways = 1
n = 2 ---> ways: (1,1) or (2) = 2
n = 3 ---> ways: (1,1,1) or (1,2) Or (2,1) = 3
n = 4 ---> ways: (1,1,1,1), (2,2), (1,2,1),(2,1,1), (1,1,2) = 5
n = 4  ---> ways = 8
.
.
.
.
.
n = k ----> ways= k-1 + k - 2



This forms a fibonacci series but one place ahead
'''
def helper(n):
    if n <= 1:
        return n
    return helper(n-1) + helper(n-2)
    

def noOfStairs(n):
    return helper(n+1)
    

n= 5
print(noOfStairs(n))