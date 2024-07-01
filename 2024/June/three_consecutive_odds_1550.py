class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        x = 0
        while x < len(arr):
            if arr[x] % 2 == 0:
                count = 0
            else:
                count+=1
                if count == 3:
                    return True
            x+=1
        return False
    