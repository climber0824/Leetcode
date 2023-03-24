struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr), {}
  ListNode(int x) : val(x), next(nullptr), {}
  ListNode(int x, ListNode *next) : val(x), next(next), {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode *dummy = new ListNode(-1);
        ListNode *curr = dummy;
        dummy->next = head;

        while (curr->next && curr->next->next) {
            ListNode *first = curr->next;
            ListNode *second = curr->next->next;
            curr->next = second;
            first->next = second->next;
            second->next = first;
            //curr = first;            pass
            curr = curr->next->next;   // beats 100%
        }
        return dummy->next;;
    }
};
