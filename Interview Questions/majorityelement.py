#Given a array return the majority element 
# Majority element's frequency is greater than (len of array / 2)

#Approach 1 (Using hash table)
#TC : O(n)
#SC : O(n)
def majorityElement(array):
    dict_ = {}
    
    for num in array:
        if num in dict_:
            dict_[num] += 1
            
        else:
            dict_[num] = 1
            
    if max(dict_.keys(),key=dict_.get):
        return max(dict_.keys(),key=dict_.get)
    
    return -1

#Approach 1 (using counter module)
#TC : O(n)
#SC : O(n)
def majorityElement(array):
    from collections import Counter
    
    dict_ = Counter(array)
    
    if max(dict_.keys(),key=dict_.get):
        return max(dict_.keys(),key=dict_.get)
    
    return -1

#Approachn 2 (Boyer - Moore Voting Algorithm)
#TC : O(n)
#SC : O(1)

def findCandidate(array):
    candidate = None
    count = 0
    
    for num in array:
        if count == 0:
            candidate = num
            
        count += (1 if num == candidate else -1)
        
    return candidate

def isMajorityElement(array,candidate):
    count = array.count(candidate)
    
    return True if count > len(array) // 2 else False

def majorityElement(array):
    candidate = findCandidate(array)
    
    if isMajorityElement(candidate):
        return candidate
    
    return -1
    