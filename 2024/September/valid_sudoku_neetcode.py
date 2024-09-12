# class Solution:
#     def isValidSudoku(self, board):
#         cols = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
#         for i, row in enumerate(board):
#             rows = {}
#             for j, v in enumerate(row):
#                 if v == '.':
#                     continue
#                 elif v in rows or v in cols[j]:
#                     return False
#                 else:
#                     rows[v] = 1
#                     cols[j][v] = 1
#         return True

                
# board = [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Solution1 = Solution()
# Solution1.isValidSudoku(board)

### FAILED ###

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # USE SETS INSTEAD OF DICTIONARIES
        rows = defaultdict(set) 
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):  
            for c in range(9): # ALWAYS 9x9, SO WE CAN JUST SET A FIXED RANGE.
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)] # # FOR THE DIAGONOLS!
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c]) 

        return True


# Had the right idea, but the wrong execution. Needed to use sets instead of dictions and set a 'Square' set that would be able to evaluate the 3x3 boxes.