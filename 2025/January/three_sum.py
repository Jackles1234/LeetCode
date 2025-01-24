class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        return_sums = []
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k-= 1
                elif total < 0:
                    j+= 1
                else:
                    return_sums.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j <k:
                        j+=1
        return return_sums

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))