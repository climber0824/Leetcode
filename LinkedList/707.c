typedef struct MyLinkedList {
    struct MyLinkedList *next;
    int val;

} MyLinkedList;

// helper function
// ____________________
size_t getNode(MyLinkedList* obj, int index) {
    MyLinkedList *curr = obj;
    int i = 0;
    while (i < index && curr) {
        curr = curr->next;
        i++;
    }
    return curr;
}

MyLinkedList* createNode(int val) {
    MyLinkedList* node = malloc(sizeof(MyLinkedList));
    node->val = val;
    node->next = NULL;
    
    return node;
}
// ____________________

MyLinkedList* myLinkedListCreate() {
    MyLinkedList* head = malloc(sizeof(MyLinkedList));
    head->next = NULL;
    
    return head;
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    MyLinkedList* curr = getNode(obj->next, index);
    return curr ? curr->val : -1;
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    MyLinkedList* newHead = createNode(val);
    newHead->next = obj->next;
    obj->next = newHead;
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    MyLinkedList* curr = obj;
    while (curr->next) {
        curr = curr->next;
    }
    curr->next = createNode(val);
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    MyLinkedList* curr = getNode(obj, index);
    if (curr) {
        MyLinkedList* newNode = createNode(val);
        newNode->next = curr->next;
        curr->next = newNode;
    }
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    MyLinkedList* curr = getNode(obj, index), *temp;
    if (curr) {
        if (curr->next && curr->next->next != NULL) {
            temp = curr->next;
            curr->next = curr->next->next;
            free(temp);

        } else if (curr->next && curr->next->next == NULL) {
            temp = curr->next;
            free(temp);
            curr->next = NULL;
        }
    }
}

void myLinkedListFree(MyLinkedList* obj) {
    MyLinkedList* curr = obj;
    while (curr->next) {
        MyLinkedList* temp = curr->next;
        curr->next = curr->next->next;
        free(temp);
    }
}
