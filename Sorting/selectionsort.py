# Comparisions = n(n-1)/2
#Swaps = n-1
#TC : O(n^2)
# first element is the first sorted element

def selectionSort(arr):
    
    
    for i in range(len(arr)):
        min_ = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_]:
                min_ = j
        arr[i],arr[min_] = arr[min_],arr[i]
            
        
    return arr
arr = [70,20,50,30,90,5,15]

print(selectionSort(arr))
            
            