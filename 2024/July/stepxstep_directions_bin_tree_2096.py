# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        def dfs(node, path, val) :
            if node.val == val :
                return True
            if node.left and dfs(node.left, path, val) :
                path.append('L')
            elif node.right and dfs(node.right, path, val) :
                path.append('R')
            return len(path) > 0 # failed to find a path
        start, dest = [], []
        dfs(root, start, startValue) # create a start node path
        dfs(root, dest, destValue) # create a dest node path
        
        while start and dest and start[-1] == dest[-1] :
            start.pop()
            dest.pop()
        
        return 'U'*len(start) + ''.join(reversed(dest))