class Solution:
    def topKFrequent(self, nums, k):
        highest_dict = {}
        for i in nums:
            if i in highest_dict:
                highest_dict[i]+=1
            else:
                highest_dict[i] = 1
        sorted_items = sorted(highest_dict.items(), key=lambda x: x[1], reverse=True)       
        top_n_keys = [key for key, value in sorted_items[:k]]
        return (top_n_keys)