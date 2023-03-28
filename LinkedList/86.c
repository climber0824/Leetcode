struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* partition(struct ListNode* head, int x){
    struct ListNode* dummy1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* dummy2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy1->val = 0;
    dummy1->next = NULL;
    dummy2->val = 0;
    dummy2->next = NULL;

    struct ListNode* p1 = dummy1;;
    struct ListNode* p2 = dummy2;

    while (head) {
        if (head->val < x) {
            p1->next = head;
            p1 = p1->next;
        } else {
            p2->next = head;
            p2 = p2->next;
        }
        head = head->next;
    }
    p1->next = dummy2->next;
    p2->next = NULL;

    return dummy1->next;
}
