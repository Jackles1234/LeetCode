class Solution(object):
    def get_comb_mean(self, rolls, return_list):
        return (sum(rolls + return_list))/(len(rolls)+len(return_list))

    def missingRolls(self, rolls, mean, n):
        return_list = [5 for _ in range(n)]
        print(self.get_comb_mean(rolls, return_list))
        if mean < self.get_comb_mean(rolls, return_list):
            return []


        

solution = Solution()
solution.missingRolls([3,2,4,3], 4, 2)