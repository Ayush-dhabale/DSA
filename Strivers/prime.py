
#Brute
#O(N)
def prime(N):
    count = 0
    
    for i in range(1,N+1):
        if N % i == 0:
            count += 1
            
        if count > 2:
            return 'Non-prime'
        
    if count == 2:
        return "Prime"
    return 'Non-prime'

#optimal
#O(N ^ 1/2)
def prime(N):
    count = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            count += 1
            
            if N // i != i:
                count += 1
                
        if count > 2:
            return 'Non-prime'
        
    if count == 2:
        return "Prime"
    return "Non - Prime"
