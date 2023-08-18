class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        vector<vector<bool>> connected(n, vector<bool>(n, false));
        vector<int> g(n, 0);
        int i, j, res = 0;
    
        for (int i = 0; i < roads.size(); i++) {
            g[roads[i][0]]++;
            g[roads[i][1]]++;
            connected[roads[i][0]][roads[i][1]] = true;
            connected[roads[i][1]][roads[i][0]] = true;
        }

        for (i = 0; i < n; i++) {
            for (j = i+1; j < n; j++) {
                int duplicate = 0;
                if (connected[i][j]) {
                    duplicate = 1;
                }
                res = max(res, g[i] + g[j] - duplicate);
            }
        }        
        return res;        
    }
};
