class Node():

    def __init__(self, val, min_, next=None):
        self.val = val
        self.min_ = min_
        self.next = next
        

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(val, self.head.min_), self.head)
        

    def pop(self) -> None:
        self.head = self.head.next
        

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:
        return self.head.min_
