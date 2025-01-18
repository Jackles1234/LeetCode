class Solution(object):
    def sortedSquares(self, nums):
        nums = [i**2 for i in nums] #square
        return sorted(nums)
    
class Solution2(object):
    def sortedSquares(self, nums):
        n = len(nums)
        ans = [0] * n
        start,end = 0, n-1
        for i in range(n-1, -1, -1):   #iterate backward through list
            if abs(nums[start]) >= abs(nums[end]): # if starting number is greater than 
                ans[i] = nums[start] * nums[start]  # add it to the next part, 
                start +=1   # start iterates +1
            else:   # end + start swap. always 1 away. 
                ans[i] = nums[end] * nums[end]  # if its smaller, add it to the next position
                end-=1  # end iterates -1

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))



