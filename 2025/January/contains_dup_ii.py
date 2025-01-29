class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()
        for i, v in enumerate(nums):
            if v in seen:
                return True
            seen.add(v)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False

sol =  Solution()
print(sol.containsNearbyDuplicate([1,2,3,1], 3))