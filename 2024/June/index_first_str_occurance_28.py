class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            count = 0
            i = 0
            while i < (len(haystack)):
                if haystack[i] == needle[count]:
                    if count == len(needle)-1:
                        return i - count
                    count+=1
                    i+=1
                else:
                    i+=1
                    i -= count
                    count = 0
        return -1
    
### CORRECT ###