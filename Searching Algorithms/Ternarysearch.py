'''
#Iterative
def ternarySearch(arr,num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid1 = low + (high - low) // 2
        mid2 = high - (high - low) // 2
        
        if arr[mid1] == num:
            return mid1
        
        elif arr[mid2] == num:
            return  mid2
        
        elif arr[mid1] > num:
            high = mid1 - 1
            
        elif arr[mid2] < num:
            low = mid2 + 1
            
        elif arr[mid1] < num and arr[mid2] > num:
            low = mid1 + 1
            high = mid2 - 1
            
        else:
            return -1
'''
#TC: O(log3(n))
#Recursive
def ternarySearch(arr,target, low , high):
    if high >= low:
        mid1 = low + (high -low) // 2
        mid2 = high - (high - low) // 2
        
        if arr[mid1] == target:
            return mid1
        
        elif arr[mid2] == target:
            return mid2
        
        elif arr[mid1] > target:
            return ternarySearch(arr,target,low, mid1 - 1)
        
        elif arr[mid2] < target:
            return ternarySearch(arr,target,mid2 + 1, high)
        
        else:
            return ternarySearch(arr,target,mid1 + 1, mid2 - 1)
        
    else:
        return -1            
result = ternarySearch([4,5,6,7,8,9,12,25],25,0,7)          
print(result)
        