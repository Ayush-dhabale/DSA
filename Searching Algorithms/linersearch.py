#TC: O(n)
#Function to search the element linearly
def linerSearch(arr,num):
    
    for i in range(len(arr)):
        if arr[i] == num:
            return i
        
    return -1

#Diver Code

if __name__ == "__main__":
    arr = [3,2,7,8,1,9,37,5]
    num = 8
    
    index = linerSearch(arr,num)
    print(index)    



    