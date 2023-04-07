class Solution {
public:
    /*
    void dfs(vector<vector<int>>& grid, int x, int y) {   
        int M = grid.size(), N = grid[0].size();     
        if (x<0 || x>=M || y<0 || y>=N || grid[x][y]==0) return;
        grid[x][y] = 0;
        dfs(grid, x+1, y);
        dfs(grid, x-1, y);
        dfs(grid, x, y+1);
        dfs(grid, x, y-1);
        
        vector<int> dx = {1, -1, 0, 0};
        vector<int> dy = {0, 0, 1, -1};
        for (int i=0; i<4; i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            if (grid[new_x][new_y] == 1) {
                dfs(grid, new_x, new_y, M, N);
            }
        }
        
    }
    */
    void dfs(vector<vector<int>>& grid, int x, int y, int val) {
        int m = grid.size(), n = grid[0].size();
        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] != 1)
            return;

        grid[x][y] = val;
        dfs(grid, x+1, y, val);
        dfs(grid, x-1, y, val);
        dfs(grid, x, y+1, val);
        dfs(grid, x, y-1, val);
         
    }
    int numEnclaves(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size();
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if ((i == 0 || i == M-1 || j == 0 || j == N-1) && (grid[i][j] == 1)) {
                    dfs(grid, i, j, 0);
                }
            }
        }
        for (int i = 1; i < M-1; i++) {
            for (int j = 1; j < N-1; j++) {
                if (grid[i][j] == 1) {                    
                    res++;
                }
            }
        }
        
        return res;
        /*
        int M = grid.size(), N = grid[0].size();
        int res = 0;
        //if (M==0 || N==0) return 0;

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if ((i==0 || i==M-1 || j==0 || j==N-1) && (grid[i][j] == 1)) {
                    dfs(grid, i, j);
                }
            }
        }
        
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == 1) {
                    res++;
                }
            }
        }
        
        return res;
        */

    }
};
