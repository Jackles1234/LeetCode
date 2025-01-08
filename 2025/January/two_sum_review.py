###1 Two Sum###

class Solution(object):
    def twoSum(self, nums, target):
        return_list = []
        nums_dict = {}
        for i, v in enumerate(nums):
            if target - int(v) in nums_dict:
                return i, nums_dict[target-v]
            else:
                nums_dict[v] = i
                


print(Solution.twoSum(0, [2,7,11,15], 9))