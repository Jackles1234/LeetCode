class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n+1) # make list n+1 long
        dp[0] = dp[1] = 1   #first and second val = 1
        
        for i in range(2, n+1): #2 -> n+1
            dp[i] = dp[i-1] + dp[i-2] #add i-1 and i-2 to the next value of i. Ultimately going to end with the final value
        return dp[n] #returns last value in list