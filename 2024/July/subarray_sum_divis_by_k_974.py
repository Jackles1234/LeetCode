class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = 0
        length = len(nums)
        if sum(nums) < k and length > 2:
            return 0
        for i in range(length):
            curr_total = 0
            for j in range(i, length):
                curr_total += nums[j]
                if curr_total %k == 0:
                    count+=1
        return count
    

## Incorrect ##

class Solution2(object):
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}
        for num in nums:
            prefix_sum += num   #curr_total
            mod = prefix_sum % k    #calculate remainder
            if mod < 0:  #if greater than 0, add k
                mod += k
            if mod in prefix_map:   #ifs its in the hash map, add the current map count to count, then add 1 to teh curr map count
                count += prefix_map[mod]
                prefix_map[mod] += 1
            else:
                prefix_map[mod] = 1 #else curr_map count == 1
        return count