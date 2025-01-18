#TC: O(log2(n))
# Iterative
def binarySearch(arr,num):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        
        elif arr[mid] > num:
            high = mid - 1
            
        else:
            low = mid + 1
            
    return -1 
            
#Recursive
def binarySearch(arr, target, low , high):
    if high >= low:
        mid = (low + high ) //2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return binarySearch(arr, target, low, mid - 1)
        
        else:
            return binarySearch(arr,target, mid + 1, high)
        
        
    else:
        return - 1
        
            

        