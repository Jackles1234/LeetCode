class Solution:
    def longestConsecutive(self, nums):
        sorted_arr = sorted(nums)
        count = 0
        for i, v in enumerate(sorted_arr):
            if v == sorted_arr[i+1] or v == sorted_arr[i+1]-1:
                count+=1
            else:
                return count
sol1 = Solution()
print(sol1.longestConsecutive([2,20,4,10,3,4,5]))