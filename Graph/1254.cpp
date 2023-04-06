class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size();
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if ((i == 0 || i == M-1 || j == 0 || j == N-1) && (grid[i][j] == 0)) {
                    dfs(grid, i, j, 1);
                }
            }
        }
        for (int i = 1; i < M-1; i++) {
            for (int j = 1; j < N-1; j++) {
                if (grid[i][j] == 0) {
                    dfs(grid, i, j, 1);
                    res++;
                }
            }
        }
        
        return res;
    }

    void dfs(vector<vector<int>>& grid, int x, int y, int val) {
        int m = grid.size(), n = grid[0].size();
        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] != 0)
            return;

        grid[x][y] = val;
        dfs(grid, x+1, y, val);
        dfs(grid, x-1, y, val);
        dfs(grid, x, y+1, val);
        dfs(grid, x, y-1, val);
         
    }
};
