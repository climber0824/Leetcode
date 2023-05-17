class Node():
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.mod = 1000
        self.node = [None] * 1000
        
    def put(self, key: int, value: int) -> None:
        idx = key % self.mod
        if self.node[idx] == None:
            self.node[idx] = Node(key, value)
        else:
            curr = self.node[idx]
            while True:
                if curr.key == key:
                    curr.key = key
                    curr.val = value
                    return
                if curr.next == None:
                    break
                curr = curr.next
            curr.next = Node(key, value)

    def get(self, key: int) -> int:
        idx = key % self.mod
        curr = self.node[idx]
        while curr:
            if curr.key == key:
                return curr.val
            else:
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.mod
        curr = prev = self.node[idx]
        if not curr: return
        if curr.key == key:
            self.node[idx] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    break
                else:
                    curr, prev = curr.next, prev.next

