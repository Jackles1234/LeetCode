class Solution(object):
    def get_comb_mean(self, rolls, return_list):
        return (sum(rolls + return_list))/(len(rolls)+len(return_list))

    def missingRolls(self, rolls, mean, n):
        for i in range(1, 6, 1):
            return_list = [i for _ in range(n)]
            print(self.get_comb_mean(rolls, return_list))
            if mean < self.get_comb_mean(rolls, return_list):
                break
        while 

        

solution = Solution()
solution.missingRolls([3,2,4,3], 4, 2)