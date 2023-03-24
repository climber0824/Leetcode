/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode {
  int val;
  struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* head) {
  if ((!head) || (!head->next))
    return head;
  
  struct ListNode *temp = head;
  head = head->next;
  temp->next = head->next;
  head->next = temp;
  head->next->next = swapPairs(head->next->next);
  
  return head;
}
  
