class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        
        prefix = [1] * n    #intitalize two arrays that will count as everything before n index, and everything after n index
        suffix = [1] * n
        
        for i in range(1, n):       #calculate prefix 1, n-1 (second-end)
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):      #calculate suffix n-2, 0, -1 (second to last to 0)
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # each array is shifted one direction away from eachother so we can get each total from either array with that index missing. 

        answer = [prefix[i] * suffix[i] for i in range(n)]  #finally, multiply all of these together for final results. 
        
        return answer