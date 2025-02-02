class Solution(object):
    def twoSum(self, nums, target):
        return_list = []
        nums_dict = {}
        for i, v in enumerate(nums):
            if target - int(v) in nums_dict:
                return i, nums_dict[target-v]
            else:
                nums_dict[v] = i

    def threeSum(self, nums):
        sorted_arr = sorted(nums)
        dupes = {}
        return_sums = []
        for i, v in enumerate(sorted_arr): 
            if v in dupes:
                continue
            else:
                self.twoSum()


        return sorted_arr
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))

#need to have set with found vals
#how to iterate x3? 