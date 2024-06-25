class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        print(position)
        for i in range(len(position)):
            for j in range(len(position)):
                dist = position[i] - position[j]
                


        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """

Solution.maxDistance(None, [1,2,3,4,7], 3)