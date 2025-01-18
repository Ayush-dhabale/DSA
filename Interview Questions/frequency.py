#Frequency of an element in a sorted array

def frequency(arr,num):
    
    low = 0
    high = len(arr) - 1
    first = last = -1
    
    while high >= low:
        mid = (low + high) // 2
        
        if arr[mid] == num :
            first = last = mid
            
            m = mid - 1
            while m >= 0 and arr[m] == num:
                first = m
                m -= 1
            
            n = mid + 1
            while n < len(arr) and arr[n] == num:
                last = n
                n += 1
                
            break
                
        elif arr[mid] > num:
            high = mid - 1
                
        else:
            low = mid + 1
            
    if first == -1 and last == -1:
        return -1
            
    return (last - first + 1)

#USing O(log(n)) complexity
def frequency(array,num):
    pass
arr = [1,4,6,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,10,14,16]
result = frequency(arr,8)
print(result)
    
            
    