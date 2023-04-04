class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        unordered_map<int, int> m;
        vector<vector<int>> res;

        for (int i : nums) m[i]++;
        while (m.size()) {
            vector<int> v;
            for (auto i : m) {                
                v.push_back(i.first);
            }
            for (int i : v) {
                if (!--m[i])
                    m.erase(i);
            }
            res.push_back(v);
        }
        return res;
    }
};
