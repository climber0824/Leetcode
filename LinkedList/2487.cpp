class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        ListNode* dummy = new ListNode(INT_MAX);
        vector<ListNode*> stack = {dummy};
        
        while (head) {
            while (!stack.empty() && head->val > stack.back()->val) {
                stack.pop_back();
            }
            stack.back()->next = head;
            stack.push_back(head);
            head = head->next;
        }
        return dummy->next;
    }
};
