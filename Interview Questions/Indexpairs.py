#Given a sorted array, return a index pair (i,j) such that array[i] + array[j] = target
#TC : O(n)

def Pairs(array,target,i,j):
    if i < j:
        if array[i] + array[j] == target:
            return [i,j]
        
        elif array[i] + array[j] > target:
            return Pairs(array,target,i,j-1)
        
        else:
            return Pairs(array,target,i+1,j)
        
    return [-1,-1]

array = [10,20,30,40,50,60,70,80,90,100]
target = 100

result = Pairs(array, target, 0, len(array) - 1)            
print(result)