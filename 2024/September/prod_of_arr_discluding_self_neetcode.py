import numpy
class Solution:
    def productExceptSelf(self, nums):
        new_arr = []
        for i in range(len(nums)):
            copy_arr = nums.copy()
            copy_arr.pop(i)
            new_arr.append(numpy.prod(copy_arr))
        return new_arr