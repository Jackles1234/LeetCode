class failedSolution(object):
    def checkLength(self, num1, num2, limit):
        if num1 - num2 <= limit:
            return True
        else:
            return False

    def longestSubarray(self, nums, limit):
        globMax = 0
        count = 0
        for i in range(len(nums)):
            localMax = 0
            while count <= len(nums):
                if self.checkLength(nums[i], nums[count], limit):
                    localMax+=1
                    count+=1
                elif localMax > globMax:
                    globMax = localMax
        return globMax

        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
### INCORRECT ###

# Very hard question that I tried to solve, but ran out of time doing. 


class Solution(object):
    def longestSubarray(self, nums, limit):
        increase = deque()
        decrease = deque()
        max_length = 0
        left = 0

        for right in range(len(nums)):
            while increase and nums[right] < increase[-1]:
                increase.pop()
            increase.append(nums[right])
            
            while decrease and nums[right] > decrease[-1]:
                decrease.pop()
            decrease.append(nums[right])
            
            while decrease[0] - increase[0] > limit:
                if nums[left] == increase[0]:
                    increase.popleft()
                if nums[left] == decrease[0]:
                    decrease.popleft()
                left += 1
                
            max_length = max(max_length, right - left + 1)
        
        return max_length