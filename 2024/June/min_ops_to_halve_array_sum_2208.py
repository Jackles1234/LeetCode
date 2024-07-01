class Solution(object):
    def halveArray(self, nums):
        operations = 0
        total = 0
        sums = sum(nums)
        nums.sort()
        while True:
            num = nums[-1] / 2
            nums[-1] - num
            total += num
            #if total += num


### INCORRECT ###

import heapq
class Solution(object):
    def halveArray(self, A):
        q, s, k, i = [], sum(A), 0, 0   #adds all nums to heap and then sorts
        for x in A:
            heapq.heappush(q, -x)
        while s - k > s / 2:    #Then tests for the nums
            x = -heapq.heappop(q)   #remvoes last element 
            k += x / 2              #divides it by two and then adds it
            heapq.heappush(q, -x / 2)
            i += 1  #operation count
        return i
    
### Kinda understood. I need to learn more about heaps to and their functionality.