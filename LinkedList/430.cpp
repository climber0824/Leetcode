class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return NULL;
        Node *curr = head;
        Node *p, *next;
        
        while (curr) {
            if (curr->child) {
                next = curr->next;
                curr->next = curr->child;
                curr->next->prev = curr;
                curr->child = NULL;
                p = curr->next;
                while (p && p->next) {
                    p = p->next;
                }
                p->next = next;
                if (next) next->prev = p;
            }
            curr = curr->next;
        }        
        return head;
    }
};
