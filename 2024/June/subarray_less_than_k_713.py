import numpy
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        count = 0
        n = len(nums)
        subarrays = []
        for start in range(n):
            for end in range(start + 1, n + 1):
                subarrays.append(nums[start:end])
        for i in range(0, len(subarrays)):
            product = numpy.prod(subarrays[i])
            if product < k:
                count+=1
        return count
    

### WRONG ANSWER ###
#Took to long and not efficient enought for leetcode

### CORRECT SOLUTION ###
#Sliding Window
class correctSolution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        ans = 0
        l,product = 0,1

        for r,num in enumerate(nums):
            print(r, k)
            product *=num
            while product>=k and l<=r:
                product//=nums[l]
                l+=1
            ans+=r-l+1
        return ans

correctSolution.numSubarrayProductLessThanK(None, [10,5,2,6], 100)