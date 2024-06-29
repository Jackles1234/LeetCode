class Solution(object):
    def finalString(self, s):
        final_str = ""
        for i in s:
            if i != 'i':
                final_str+= i
            else:
                final_str = final_str[::-1]
        return final_str

### CORRECT ###