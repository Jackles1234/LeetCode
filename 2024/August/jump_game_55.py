class Solution(object):
    def canJump(self, nums):
        count = 0
        for i in range(len(nums)):
            if count < 0:
                return False
            elif nums[i] > count:
                count = nums[i]
            count-=1
        return True