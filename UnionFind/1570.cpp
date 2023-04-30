class DSU {
public:
    vector<int> parent, rank;

    DSU(int n) {
        parent.resize(n, 0);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int Find(int x) {
        if (x != parent[x]) {
            parent[x] = Find(parent[x]);
        }
        return parent[x];
        //return parent[x] = parent[x] == x ? x : Find(parent[x]);
    }

    bool Union(int x, int y) {
        int x_root = Find(x), y_root = Find(y);
        if (x_root != y_root) {
            rank[x_root] < rank[y_root] ? parent[x_root] = y_root : parent[y_root] = x_root;
            rank[x_root] += rank[x_root] == rank[y_root];
            return true;
        }
        return false;
    }

};

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        sort(edges.begin(), edges.end(), [&](auto const &a, auto const &b){
            return a[0] > b[0];
        });

        DSU dsu_alice(n + 1);
        DSU dsu_bob(n + 1);

        int removed_edges = 0, alice_edges = 0, bob_edges = 0;
        for (auto edge : edges) {
            if (edge[0] == 3) {
                if (dsu_alice.Union(edge[1], edge[2])) {
                    dsu_bob.Union(edge[1], edge[2]);
                    alice_edges++;
                    bob_edges++;
                } else {
                    removed_edges++;                    
                }
            }
            else if (edge[0] == 1) {
                if (dsu_alice.Union(edge[1], edge[2])) {
                    alice_edges++;
                } else {
                    removed_edges++;
                }
            }
            else {
                if (dsu_bob.Union(edge[1], edge[2])) {
                    bob_edges++;
                } else {
                    removed_edges++;
                }
            }
        }

        return (bob_edges == n - 1 && alice_edges == n - 1) ? removed_edges : -1;
    }
};
