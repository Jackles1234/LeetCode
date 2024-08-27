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
        ans = 0 #return val
        l,product = 0,1 # l = start of sliding window, product = prod of currrent elements in current window

        for r,num in enumerate(nums):   # r = end of sliding window, num = current number from the array 'nums'
            #print(r, k)
            product *=num   # as r moves from end to end of array, it is multiplied by last product to get full value of array
            while product>=k and l<=r:
                product//=nums[l]
                l+=1
            ans+=r-l+1
        return ans
#Once product is less than k again, the number of new valid subarrays that include the element at r is r - l + 1. This is because each element from l to r can form a subarray ending at r that has a product less than k. For example, if l is 0 and r is 2, the valid subarrays are [nums[2]], [nums[1], nums[2]], and [nums[0], nums[1], nums[2]].
correctSolution.numSubarrayProductLessThanK(None, [10,5,2,6], 100)