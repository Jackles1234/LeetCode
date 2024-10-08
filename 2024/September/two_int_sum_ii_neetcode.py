class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:    #Binary Search
            curSum = numbers[l] + numbers[r]    

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

 ### INCORRECT ###