/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
    if (!head) return head;
    struct ListNode* prev;
    struct ListNode* curr;
    struct ListNode* dummy;
    prev = curr = dummy = head;
    curr = curr->next;
    while (prev && curr) {
        while (curr && curr->val == prev->val) {
            curr = curr->next;
        }
        prev->next = curr;
        prev = prev->next;
    }
    return dummy;
}
