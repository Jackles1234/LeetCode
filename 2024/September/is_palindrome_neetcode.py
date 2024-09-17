import re
class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        rev_str = ""
        for i in s:
            rev_str = i+rev_str
        if rev_str == s:
            return True
        else:
            return False