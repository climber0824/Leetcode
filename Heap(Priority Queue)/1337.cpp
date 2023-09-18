struct compareHeapElements {
    bool operator()(pair<int,int> const& p1, pair<int,int> const& p2) {
        if (p1.first < p2.first) {
            return true;
        } else if (p1.first == p2.first && p1.second < p2.second) {
            return true;
        }
        return false;
    }
};

class Solution {
public:
    int soldierCount(vector<int> &v) {
        int l = 0, r = v.size() - 1;
        while (l <= r) {
            int mid = l + (r-l) / 2;
            if (v[mid] == 0) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        priority_queue<pair<int,int>, vector<pair<int,int>>, compareHeapElements> max_heap;
        for (int i = 0; i < mat.size(); ++i) {
            max_heap.push({soldierCount(mat[i]), i});
            if (max_heap.size() > k) {
                max_heap.pop();
            }
        }
        vector<int> res;
        while (max_heap.size()) {
            res.push_back(max_heap.top().second);
            max_heap.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
