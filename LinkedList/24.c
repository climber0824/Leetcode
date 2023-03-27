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
  struct ListNode* temp = head;
    while (temp && temp->next)
    {
        if (temp->next->val == temp->val)
        {
            temp->next = temp->next->next;
            continue;
        }
        temp = temp->next;
    }
    return head;
  /*
  if ((!head) || (!head->next))
    return head;
  
  struct ListNode *temp = head;
  head = head->next;
  temp->next = head->next;
  head->next = temp;
  head->next->next = swapPairs(head->next->next);
  
  return head;
  */
}
