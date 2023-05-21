"""
First using DFS to find island1, 
then using BFS to expaned the island1 until reaching island2.
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def dfs(x, y, island1):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = -1
            island1.append([x, y])
            for dx, dy in dirs:
                newX, newY = x + dx, y + dy
                dfs(newX, newY, island1)

        res = 0
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        n = len(grid)
        island1 = []
        found = False
        for i in range(n):
            for j in range(n):                          
                if grid[i][j] == 1:                    
                    dfs(i, j, island1)
                    found = True   # find island1                              
                    break          # prevent island2 to set to -1
            if found:
                break              # break the for-loop

        while island1:
            new_island = []
            for i, j in island1:
                for dx, dy in dirs:
                    newX, newY = i + dx, j + dy
                    if 0 <= newX < n and 0 <= newY < n:
                        if grid[newX][newY] == 1:       # find island2
                            return res                
                        elif not grid[newX][newY]:      # where the cell is zero
                            grid[newX][newY] = -1
                            new_island.append([newX, newY])
            res += 1
            island1 = new_island  # the new expanded island
        return res

        """

        def dfs(i, j):
            A[i][j] = -1
            bfs.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j
        n, step, bfs = len(A), 0, []
        dfs(*first())
        print(bfs)
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            bfs = new
        """
