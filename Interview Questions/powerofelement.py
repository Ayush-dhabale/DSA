#TC : O(log(n))

#Given a nums a and 'a' interger 'n' return a^n

def Power(a,n):
    if n < 0:
        a = 1 / a
        n = -n
        
    if n==1:
        return a
    
    else:
        mid = n // 2
        
        result = Power(a,mid)
        result *= result
        
        if n % 2 == 0:
            return result
        
        return result*a
    
a = 2
n = 10
result = Power(a,n)
print(result)
            