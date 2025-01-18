#Sorted matrix(first element of each row in greater than than last element of  previous row)

def matrixSearch(arr,num):
    
    low =  0
    high = len(arr[0]) * len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        row = mid // len(arr[0])
        column = mid % len(arr)
        
        if arr[row][column] == num:
            return row + 1, column + 1
        
        elif arr[row][column] > num:
            high = mid - 1
            
        else:
            low = mid + 1
            
    return - 1, -1
            
arr = [
    [1,3,5],
    [7,10,11],
    [16,20,23]
]

i,j = matrixSearch(arr,2)

print(i,j)