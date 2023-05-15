/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {        
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* headPtr = head;
        int count = k;
        int temp1, temp2;
        while (k > 1) {
            fast = fast->next;
            k--;
        }
        temp1 = fast->val;        
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next;
        }
        temp2 = slow->val;        
        slow->val = temp1;
        while (count > 1) {
            headPtr = headPtr->next;
            count--;
        }
        headPtr->val = temp2;
        return head;
    }
};
