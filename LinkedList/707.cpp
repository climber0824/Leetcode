class Node {
public:
    int val;
    Node* next;
    // Constructor of Node
    // below are queal
    // Node(int x): val(x), next(nullptr) {}
    Node(int x) {val=x; next=nullptr;}
};


class MyLinkedList {
public:
    Node* head;
    int size;
    
    // Constructor
    MyLinkedList() {
        head = nullptr;
        size = 0;        
    }
    
    int get(int index) {
        if (index >= size || index < 0) return -1;
        Node* curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        return curr->val;
    }
    
    void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    void addAtTail(int val) {
        addAtIndex(size, val);        
    }
    
    void addAtIndex(int index, int val) {        
        if (index < 0 || index > size) return;

        Node* curr = head;
        Node* newNode = new Node(val);
        if (index == 0) {
            newNode->next = curr;
            head = newNode;
        } else {
            for (int i = 0; i < index - 1; i++) {
                curr = curr->next;
            }                          
            newNode->next = curr->next;
            curr->next = newNode;            
        }
        size++;
    }
    
    void deleteAtIndex(int index) {
        // 1 2 3 4 5 6 ; 3      
        if (index >= size || index < 0) return;
        
        if (index == 0) {
            Node* nextNode = head->next;
            delete head;
            head = nextNode;
        } else {
            Node* curr = head;
            for (int i = 0; i < index - 1; i++) {
                curr = curr->next;
            }
            Node* temp = curr->next->next;
            delete curr->next;
            curr->next = temp;
        }
        size--;
    }
};
