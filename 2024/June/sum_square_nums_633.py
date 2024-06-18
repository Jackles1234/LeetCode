class Solution1(object):
    def judgeSquareSum(self, c):
        a = 1
        b = 1
        while c >= ((a**2) + (b**2)):
            print(a,b)
            if ((a**2) + (b**2)) == c:
                return True
            else:
                b+=1
        return False
    

class Solution2(object):
    def judgeSquareSum(self, c):

        a = 0
        b = 0
        while a <= c and b <= c:
            if ((a**2) + (b**2)) == c:
                return True
            elif ((a**2) + (b**2)) > c:
                b = 0
                a+=1
            elif b >= c:
                b = 0
                a+=1
            else:
                b+=1
        return False


print(Solution1.judgeSquareSum(1, 5))
print(Solution2.judgeSquareSum(1, 5))


#INCORRECT. 1. fails under 4 because it needs a 0 number. Solution 1 was mainly used for testing if my thinking was correct so I expected it to fail after a bit. 
#Solution 2 also fails as it takes to long to iterate through values. 

###CORRECT SOLUTION###
import math
class Solution(object):
    def judgeSquareSum(self, c):
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            if left * left + right * right == c:
                return True
            elif left * left + right * right > c:
                right -= 1
            else:
                left += 1
        return False
    
## This solution is a great way to solve this question. I am thinking in brute force terms but I should think in simpler terms. This solution solves from both ends to save on time complexity and allows to come to a solution faster. 
    
