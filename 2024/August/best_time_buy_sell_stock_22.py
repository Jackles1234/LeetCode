class Solution(object):
    def maxProfit(self, prices):
        max = 0
        start = prices[0]
        len1 = len(prices)
        for i in range(len1):
            if start < prices[i]: 
                max += prices[i] - start
            start = prices[i]
        return max
    

# Incorrect. 

# You can always just check if the numeber before is smaller and make a profit regardless. 
