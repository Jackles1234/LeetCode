### 1266 Minimum Time Visiting All Points ###

class Solution(object):
    def move_vert(self, pos, dest):
        if pos[1] > dest[1]:
            pos[1] -=1
        else:
            pos[1] +=1
        return pos
    def move_horz(self, pos, dest):
        if pos[0] > dest[0]:
            pos[0] -=1
        else:
            pos[0] +=1
        return pos
    
    def minTimeToVisitAllPoints(self, points):
        seconds = 0
        pos = points[0]
        for dest in points:
            while pos != dest:
                if pos[0] != dest[0]:
                    if pos[1] != dest[1]:
                        pos = self.move_vert(pos, dest)
                    pos = self.move_horz(pos, dest)
                else:
                    pos = self.move_vert(pos, dest)
                seconds+=1
        return seconds
# GREAT, but very slow. 

class Solution2(object):
    def minTimeToVisitAllPoints(self, points):
        seconds = 0
        x1, y1 = points.pop()

        while points:
            x2, y2 = points.pop()
            seconds +=  max(abs(y2-y1), abs(x2-x1)) #always have to move 1 whether it be diagonal, horizontal or vertical. 
            # just find biggest number that it is going take, then add it. Faster than bf 'ing the solution.
            x1, y1 = x2, y2
        return seconds

sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))

sol2 = Solution2()

print(sol2.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))