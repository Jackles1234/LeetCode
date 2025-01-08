###268 Missing Number###
class Solution(object):
    def missingNumber(self, nums):
        nums = sorted(nums)  #VERY SLOW!
        for i, v in enumerate(nums):
            if i != v:
                return v-1
        return len(nums)
class Solution2(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)
        

print(Solution.missingNumber(0 ,[0,1]))
print(Solution2.missingNumber(0 ,[0,1]))