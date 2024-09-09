class Solution:
    def groupAnagrams(self, strs):
        return_list = {}
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in return_list:
                return_list[sorted_str].append(i)
            else:
                return_list[sorted_str] = [i]
        return list(return_list.values())
