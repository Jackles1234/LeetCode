###INCORRECT###

class Solution(object):
    def sortColors(self, nums):

        for color in range(((len(nums)))):
            if nums[color] == 0:
                del nums[color]
                nums.insert(0, 0)
            elif nums[color] == 1:
                del nums[color]
                nums.insert(((len(nums)))//2, 1)
            elif nums[color] == 2:
                del nums[color]
                nums.insert(-1, 2)



#Above code does not work because it does not work for arrays >2. 

#This was the simpliest solution I could find that works:

def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1

        for i in range(n):
            if i < zeros:
                nums[i] = 0
            elif zeros <= i < zeros + ones:
                nums[i] = 1
            else:
                nums[i] = 2


#This deals with the zeros and ones first and then inserts based on the zeros and ones variables. Whaterver after is twos. 