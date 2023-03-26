struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !k) return head;
        ListNode* last = head;
        int L = 1;
        while (last->next) {
            last = last->next;
            L += 1;
        }
        last->next = head;
        for (int i = 0; i < (L - k % L); i++) {
            last = last->next;
        }
        ListNode* dummy = last->next;
        last->next = nullptr;

        return dummy;
    }
};
