class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        int res = 1;
        if (grid[0][0] == 1 or grid[n-1][n-1] == 1) {
            return -1;
        }
        queue<pair<int, int>> q;
        q.push(make_pair(0, 0));
        vector<vector<int>> dirs = {{-1,0},{-1,1},{-1,-1},{0,1},{0,-1},{1,-1},{1,0},{1,1}};
        grid[0][0] = 1;
        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int x = curr.first, y = curr.second;
            if (x==n-1 && y==n-1) return grid[x][y];

            for (auto dir : dirs) {
                int i = x + dir[0];
                int j = y + dir[1];
                if (i >= 0 && i < n && j >= 0 && j < n && grid[i][j]==0) {
                    q.push(make_pair(i, j));
                    grid[i][j] = grid[x][y] + 1;
                }
            }            
        }
        return -1;
    }
};
