###217 Contains Duplicates###
class Solution(object):
    def containsDuplicate(self, nums):
        dupes = {}
        for i in nums:
            if i in dupes:
                return True
            else:
                dupes[i] = None
        return False

class Solution2(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

print(Solution.containsDuplicate(0, [1,2,3,4]))
print(Solution2.containsDuplicate(0, [1,2,3,4]))

