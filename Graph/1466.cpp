class Solution {
public:
    
    unordered_map<int, unordered_set<int>> out, in;
    int ans = 0;
    unordered_map<int,int> vis;

    void dfs(int node) {
        vis[node] = 1;
        for (int x : out[node]) {
            if (vis[x])
                continue;
            ans++;
            dfs(x);
        }
        for (int x : in[node]) {
            if (vis[x])
                continue;
            dfs(x);
        }

    }



    int minReorder(int n, vector<vector<int>>& connections) {
        ans = 0;
        for(auto c : connections) {
            out[c[0]].insert(c[1]);
            in[c[1]].insert(c[0]);
        }
        dfs(0);

        return ans;

        /* //bfs
        int res = 0;
        vector<vector<int>> out(n);
        vector<vector<int>> in(n);
        vector<int> reachRoot(n, 0);
        queue<int> q;
        q.push(0);

        for (auto& c : connections) {
            out[c[0]].push_back(c[1]);
            in[c[1]].push_back(c[0]);
        }
        
        //Use bi-directional BFS traversal of network from zero to count all paths that need to be reversed and then return changes
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            reachRoot[cur] = 1;

            //If paths from source go toward the outer node, note a change is needed
            for (auto& u : out[cur]) {
                if (reachRoot[u] == 0) {
                    res++;
                    q.push(u);
                }        
            }
            
            //If path comes toward zero, no change needed, mark for traversal
            for (auto& v : in[cur]) {
                if (reachRoot[v] == 0)
                    q.push(v);
            }
        }
        return res;       
        */
    }
};
