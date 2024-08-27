class Solution(object):
    def findCenter(self, edges):
        node_0 = edges[0][0]
        node_1 = edges[0][1]
        node_2 = edges[1][0]
        node_3 = edges[1][1]


        if node_0 == node_2:
            return node_0
        elif node_0 == node_3:
            return node_0
        elif node_1 == node_2:
            return node_1
        elif node_1 == node_3:
            return node_1
        
### CORRECT ###