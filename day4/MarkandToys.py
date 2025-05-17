def maximumToys(prices, k):
    # Write your code here
    
    prices.sort()
    i = 0
    s = 0
    
    while i < n and s + prices[i] <= k:
        s += prices[i]
        i+=1
    return i