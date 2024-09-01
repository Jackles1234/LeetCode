
# class Solution(object):
#     def construct2DArray(self, original, m, n):
#         if m*n != len(original):
#             return []  
#         d = [[ original[y] for y in range( m ) ] for x in range( n ) ]
#         print(d) 


##INCORRECT###

import numpy as np
class Solution(object):
    def construct2DArray(self, original, m, n):
        if m*n != len(original):
            return []
        
        arr2D = np.array(original).reshape(m, n)
        return arr2D.tolist()

print(Solution.construct2DArray(None, [1,2,3,4], 2, 2))

##Can use the np.reshape to make a 2d array with mxn parrameters. 