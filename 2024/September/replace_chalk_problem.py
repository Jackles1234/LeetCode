# def chalkReplacer(chalk, k):
#     x = sum(chalk)
#     temp = k % x
#     if temp > len(chalk):
#         temp-=len(chalk)
#     print(temp)
# chalkReplacer([3,4,1,2], 25)


### INCORRECT #### 
import bisect
class Solution:
    def chalkReplacer(self, chalk, k):
        for i in range(1, len(chalk)):
            chalk[i]+=chalk[i-1]
        k%=chalk[-1]
        return bisect.bisect_right(chalk, k)