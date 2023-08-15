struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        /*
        // sol1:
        ListNode less(0), greater(0);
        ListNode *lessPtr = &less, *greaterPtr = &greater;
        while (head != NULL) {
            cout << head->val << endl;
            if (head->val < x) {
                lessPtr->next = head;
                lessPtr = lessPtr->next;
            } else {
                greaterPtr->next = head;
                greaterPtr = greaterPtr->next;
            }
            head = head->next;
        }
        greaterPtr->next = NULL;
        lessPtr->next = greater.next;

        return less.next;        
        */
        // sol2
        ListNode* less = new ListNode();
        ListNode* greater = new ListNode();
        ListNode *lessPtr = less, *greaterPtr = greater;
        
        while (head) {
            if (head->val < x) {
                lessPtr->next = head;
                lessPtr = lessPtr->next;
            } else {
                greaterPtr->next = head;
                greaterPtr = greaterPtr->next; 
            }
            head = head->next;
        }
        lessPtr->next = greater->next;
        greaterPtr->next = NULL;
        
        return less->next;
    }
};
