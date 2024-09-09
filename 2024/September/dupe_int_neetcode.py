class Solution:
    def hasDuplicate(self, nums):
        dup_dict = {}
        for i in nums:
            if i not in dup_dict:
                dup_dict[i] = i
            else:
                return True
        return False