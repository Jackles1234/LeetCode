#####################INCORRECT###########################

# class Solution(object):
#     def moveZeroes(self, nums):
#         zero_indexs = []
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 zero_indexs.append(i)
#                 nums.append(0)
#         print(zero_indexs)
#         for j in zero_indexs:
#             print(j)
#             del nums[j]


# class Solution2(object):
#     def moveZeroes(self, nums):
#         count = 0
#         while count != len(nums):
#             if nums[count] == 0:
#                 del nums[count]
#                 nums.append(0)
#                 count-=1
#             count+=1

#########################################################

#Correct answer used a basic sorting algorithm to just move all the zeros to the right and move all non zeros the nearest non-zero. Different approach than I was thinking but good to know!
#CORRECT ANSWER:


class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums