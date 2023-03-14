class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int total = 0;
        ListNode *prev = NULL, *curr = head;
        vector<ListNode*> res(k, nullptr);
        while (curr) {
            total++;
            curr = curr->next;
        }
        int size = total / k, remaining = total % k;
        curr = head;
        for (int i = 0; i < k; i++, --remaining) {
            res[i] = head;
            for (int j = 0; j < size + (remaining > 0); j++) {
                prev = head;
                head = head->next;
            }
            if (prev) prev->next = NULL;
        }
        return res;
    }
};
