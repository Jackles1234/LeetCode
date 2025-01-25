class Solution(object):
    def longestMountain(self, arr):
        count = 0
        for i in range(1, len(arr)-1):  #start +1
            if arr[i-1] < arr[i] > arr[i+1]:    #if we are at peak (l and r smaller)
                l=r=i
                while l>=0 and arr[l] > arr[l-1]:   #keep checking if left is smaller contiually
                    l-=1
                while r<= len(arr)-1 and arr[r] > arr[r+1]: #keep checking if right is smaller contiually
                    r+=1
                count = max(count, r-l+1)   #max count is returned
        return count


sol = Solution()
print(sol.longestMountain([2,1,4,7,3,2,5]))