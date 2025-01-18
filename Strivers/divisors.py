#return all the divisors of a given number
'''
#Brute
# O(N)
def Divisor(N):
    result = []
    for i in range(1,N+1):
        if N % i == 0:
            result.append(i)
            
    return result
'''
#Optimal
#O(N ^ 1/2)
def Divisor(N):
    result = []
    
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            result.append(i)
            if N // i != i:
                result.append(N // i)
                
    return result

#Driver Code
N = 36
divisors = Divisor(N)
print(divisors)