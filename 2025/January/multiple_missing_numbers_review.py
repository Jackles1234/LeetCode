###448 Find all Numbers Disappeared in an Array###
class Solution(object):
    def findDisappearedNumbers(self, nums):
        set_nums = set(nums)
        return_list = []
        # Don't need new list, can just iterate through nums and check set. 
        for i in range(1, len(nums) + 1): #1 indexed, so must go 1 forward
            if i not in set_nums:
                return_list.append(i)
        return return_list
    
print(Solution.findDisappearedNumbers(0, [4,3,2,7,8,2,3,1]))