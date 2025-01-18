#A array is given, we have to find k most frequent elements(elements with highest frequency)
def mostFrequentelements(array,k):
    from collections import Counter
    import heapq
    
    dict_ = Counter(array)
    return heapq.nlargest(k,dict_.keys(),key= dict_.get)

array = [1,1,1,1,2,2,3,3,3,4,3,4,2,4,2,4]
print(mostFrequentelements(array,2)) 