from string import ascii_lowercase
class Solution(object):
    def transform(self, num_str):
        split_nums = sum([int(char) for char in num_str])
        return str(split_nums)
    def getLucky(self, s, k):   
        num_str = ""
        for i in s:
            num_str+= str(ord(i) - 96)

        for i in range(k):
            num_str = self.transform(num_str)
        return int(num_str)


### CORRECT ###