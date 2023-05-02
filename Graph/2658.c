#define MAX(a,b) (a) > (b) ? (a) : (b)
const int dir[4][2] = {{1,0}, {0,1}, {-1,0}, {0,-1}};

void dfs(int ** grid, int r, int c, int rSize, int cSize, int *cnt) {
    if (r < 0 || r >= rSize || c < 0 || c >= cSize || grid[r][c] == 0) {
        return;
    }
    (*cnt) += grid[r][c];
    grid[r][c] = 0;
    for (int i = 0; i < 4; i++) {
        dfs(grid, r+dir[i][0], c+dir[i][1], rSize, cSize, cnt);
    }
}

int findMaxFish(int** grid, int gridSize, int* gridColSize){
    int ans = 0, cnt = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] != 0) {
                dfs(grid, i, j, gridSize, gridColSize[i], &cnt);
                ans = MAX(cnt, ans);
                cnt = 0;
            }            
        }
    }
    return ans;
}
