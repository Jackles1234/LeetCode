class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        final_list = []
        freq = {}
        for i in arr1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            
        for i in arr2:
            if i in freq:
                final_list.extend([i] * freq[i])
                del freq[i]

        for i in sorted(freq.keys()):
            final_list.extend([i] * freq[i])
        
        return final_list
        

#####SORTA CORRECT####
#Was failing on the final submit and needed to refer to a solution to edit my final answer. 