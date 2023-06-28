class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        vector<vector<pair<int, double>>> g(n);
        vector<int> seen(n, 0);
        priority_queue<pair<double, int>> q;
        q.push({(double)1.0, start});
        vector<double> mx(n, (double)0.0);
        mx[start] = 1.0;

        for (int i = 0; i < edges.size(); i++) {
            g[edges[i][0]].push_back({edges[i][1], succProb[i]});
            g[edges[i][1]].push_back({edges[i][0], succProb[i]});
        }

        while (!q.empty()) {
            auto cur = q.top();
            q.pop();
            double prob = cur.first;
            int node = cur.second;
            if (!seen[node]) {
                seen[node]++;
                for (auto &nei : g[node]) {
                    if (mx[nei.first] < nei.second * prob) {
                        mx[nei.first] = nei.second * prob;
                        q.push({mx[nei.first], nei.first});
                    }
                }
            }
        }
        return mx[end];

    }
};
