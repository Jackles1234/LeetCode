class Solution(object):
    def minSteps(self, n):

        dp = [0] * (n + 1)
        
        # Loop through each number from 2 to n
        for i in range(2, n + 1):
            # Start by assuming the worst case (i.e., copying 'A' one by one)
            dp[i] = i
            # Check for divisors
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
        
        # The answer will be in dp[n]
        return dp[n]



#### INCORRECT ###
# Did not solve and had to look at a solution. 

