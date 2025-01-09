###1365 How Many Numbers Are Smaller Than the Current Number ###

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        temp = {}

        for i, v in enumerate(sorted_nums):
            if v not in temp:
                temp[v] = i
        print(temp)
        return_list = []

        for i in nums:
            return_list.append(temp[i])
        return return_list
    
print(Solution.smallerNumbersThanCurrent(0, [8,1,2,2,3]))
