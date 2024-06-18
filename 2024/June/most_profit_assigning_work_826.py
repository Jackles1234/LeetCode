###INCORRECT###

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        total_prof = 0
        curr_prof = 0
        curr_worker = 0
        for i in range(len(profit)):
            if worker[curr_worker] >= difficulty[i]: #If current Worker is greater than/equal to difficulty
                if curr_prof < profit[i]: #If selected profit is greater than current profit
                    curr_prof = profit[i]
            elif curr_worker < len(worker): #Else if, the curr work
                total_prof += curr_prof
                curr_worker+=1
                curr_prof = 0
        return total_prof 
    

###Explanation
# - Could not figure out why my solution was not working, but I tried to solve in O(n) time. The original solution O(n^2) did not work under Leetcode constraints


###CORRECT ANSWER###
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        ans = 0
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        maxProfit = 0
        j = 0
        for i in range(len(worker)):
            while j < len(jobs) and jobs[j][0] <= worker[i]:
                maxProfit = max(maxProfit, jobs[j][1])
                j += 1
            ans += maxProfit
        
        return ans
    
#This is techincally O(log(n)) because the while loop is only searching a small portion of the jobs and allows for a faster solve. 
        