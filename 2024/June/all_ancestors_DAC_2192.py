class Solution(object):
    def getAncestors(self, n, edges):
        a = [[] for _ in range(n)]
        for i in range(len(edges)):
            a[edges[i][1]].append(edges[i][0])
        print(a)
        for i in range(len(a)):
            if a[i]:
                for j in range(len(a[i])):
                    print(a[i][j])
                    #print(a[a[i][j]])
                    if a[a[i][j]]:
                       #print(a[a[i][j]])
                       a[i].extend(a[a[i][j]])
                       a[i].sort()
        print(a)
Solution.getAncestors(None, 8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])



### INCORRECT ###

class Solution(object):
    def getAncestors(self, n, edges):
        res = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
        
        for i in range(n):
            self.dfs(graph, i, i, res, [False] * n)
        
        for i in range(n):
            res[i].sort()
        
        return res
    
    def dfs(self, graph, parent, curr, res, visit):
        visit[curr] = True
        for dest in graph[curr]:
            if not visit[dest]:
                res[dest].append(parent)
                self.dfs(graph, parent, dest, res, visit)
