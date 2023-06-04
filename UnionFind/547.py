class DSU:

    def __init__(self, n):
        self.parent = {i : i for i in range(n)}        
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py

class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        g = defaultdict(set)
        res = set()
        uf = DSU(n)
        
        for i in range(n):
            for j in range(i+1):
                if grid[i][j] == 1:
                    uf.union(i, j)   
        for i in range(n):        
            res.add(uf.find(i))

        return len(res)
