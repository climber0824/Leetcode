class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        int l = 0, r = costs.size() - 1;
        long long res = 0;
        // 改變priority_queue的優先權定義：
        // priority_queue<T, vector<T>, greater<T> > pq;  改成由小排到大
        priority_queue<int, vector<int>, greater<int>> pq1, pq2;

        for (int i = 0; i < k; i++) {
            while (pq1.size() < candidates && l <= r) {
                pq1.push(costs[l++]);
            }
            while (pq2.size() < candidates && l <=r) {
                pq2.push(costs[r--]);
            } 
            int t1 = pq1.size() > 0 ? pq1.top() : INT_MAX;
            int t2 = pq2.size() > 0 ? pq2.top() : INT_MAX;

            if (t1 <= t2) {
                res += t1;
                pq1.pop();
            } else {
                res += t2;
                pq2.pop();
            }        
        }
        return res;
    }
};
