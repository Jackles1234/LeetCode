class Solution(object):
    def findTheWinner(self, n, k):
        winner = 0
        for i in range(1, n+1):
            winner = (winner+k) % i
        return winner + 1
    

#Kinda correct

#needed to adjust the for loop with a solution and had to reference a book to remember how this worked. 