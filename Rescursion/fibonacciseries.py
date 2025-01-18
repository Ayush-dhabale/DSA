'''
#Recursive Approach
def fibonacciSeries(num):
    if num <= 1:
        return num
    return fibonacciSeries(num-1) + fibonacciSeries(num-2)
'''
#Iterative Approach
def fibonacciSeries(num):
    
    a = i = sum_ = 0
    b  = 1
    
    while i < num:
        a = b
        b = sum_
        sum_ = a + b
        i += 1
        
    return sum_

num = 10
result = []
for i in range(num):
    result.append(fibonacciSeries(i))
    
print(result)
