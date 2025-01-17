import math
class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        maxP = 0
        while r!= len(prices):  #
            if prices[l] < prices[r]: #if we can get a profit
                # we are using "Greedy Alg" because we are calculating at each stage of our problem. 
                prof = prices[r] - prices[l] #calculate that profit
                maxP = max(maxP, prof)  #is that profit greater than current profit?
            else:
                l = r   #iterate by one left
            r+=1    #iterate by one on right
        return maxP

s = Solution()
print(s.maxProfit([7,6,4,3,1]))

### wrong ###