### 54 Sprial Matrix ###

# class Solution(object):
#     def spiralOrder(self, matrix):
#         spiral_return = matrix[0]
#         # doown
#         for i, v in enumerate(matrix[1:]):
#             spiral_return.append(v[-1])
#         spiral_return += (matrix[-1][-2::-1])

#         for i in 
#         return spiral_return

class Solution(object):
    def spiralOrder(self, matrix):
        return_list = []

        while matrix:
            #1 add first row, then remove
            return_list += (matrix.pop(0)) 
            #2 append lat elements of all lists
            if matrix and matrix[0]:    #checks if matrix is finished and if there is still a list
                for row in matrix:
                    return_list.append(row.pop())   #pop automatically grabs last element
            #3 add inverse of last row
            if matrix:
                return_list += (matrix.pop()[::-1])   #adds list minus last element, then removes
            #4 append first element of all rows
            if matrix and matrix[0]:        #checks if matrix is finished and if there is still a list
                for row in matrix[::-1]:        # for the next availible row in matrix, take every val minus last val
                    return_list.append(row.pop(0))  

        return return_list
sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))