#Given an array, affter some elements the array have multiple 'inft' nums, give the index of first occuring 'inf' num
#[2,-4,6,8,-9,'inf','inf','inf','inf']

def infinitenum(arr,target = 'inf'):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            if mid > 0:
                if arr[mid - 1] == target:
                    high = mid - 1
                
                
                else:
                    return mid
            else:
                return 0
            
        else :
            low = mid + 1
    return -1 
    
            
            
result = infinitenum(['inf','inf','inf','inf'],'inf')
print(result)
            
        
            