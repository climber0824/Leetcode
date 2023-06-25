class Solution {
public:
    const int MOD=1000000007;

    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        int n = locations.size();
        vector<vector<int>> dp(n, vector<int>(fuel+1, -1));

        return helper(locations, start, finish, fuel, dp); 
    }
    int helper(vector<int>& locations, int curr, int finish, int fuel, vector<vector<int>>& dp) {
        if (fuel < 0) return 0;
        if (dp[curr][fuel] != -1) {
            return dp[curr][fuel];
        }
        int ans = curr == finish ? 1 : 0;

        for (int next = 0; next < locations.size(); next++) {
            if (next != curr && fuel >= abs(locations[next] - locations[curr])) {
                ans = (ans + helper(locations, next, finish, fuel - abs(locations[next] - locations[curr]), dp)) % MOD ;
            }
        }        
        dp[curr][fuel] = ans;
        
        return ans;
    }
};
