#Recurrence Relation --> T(n) = T(n-1) + c
#TC = O(n)
'''
#Recursive

def findfactorial(num):
    if num == 1 or num == 0:
        return 1
    
    return findfactorial(num-1) * num
'''
#Iterative
def findFactorial(num):
    if num == 0 or num == 1:
        return 1
    factorial = 1
    
    while num >= 2:
        factorial *= num
        num -= 1
        
    return factorial
result = findFactorial(45)
print(result)