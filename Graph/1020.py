class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        self.res = 0

        def dfs(x, y):
            if x < 0 or x >= M or y < 0 or y >= N or grid[x][y] == 0:
                return
            grid[x][y] = 0            
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for i in range(4):                
                new_x = x + dx[i]
                new_y = y + dy[i]                
                dfs(new_x, new_y)               
        
        for i in range(M):
            for j in range(N):
                if(i == 0 or i == M-1 or j == 0 or j == N-1) and grid[i][j] == 1:
                    dfs(i, j)
        
        for i in range(M):
            for j in range(N):
                if (0 <= i < M and 0 <= j < N) and (grid[i][j] == 1):
                    self.res += 1

        return self.res 
