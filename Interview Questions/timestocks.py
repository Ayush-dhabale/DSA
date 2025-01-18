#Array of prices of stacks is given calculate the max profit one can earn
def maxProfit(arr):
    minprice = arr[0]
    maxprofit = 0
    
    for price in arr[1:]:
        if price < minprice:
            minprice = price
        else:
            maxprofit = max(maxprofit,price - minprice)
        
    return maxprofit

Prices = [7,1,5,3,6,14,4,19]

result = maxProfit(Prices)
print(result)