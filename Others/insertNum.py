"""
Given : string including 'L' and 'R'
Return: array of nums

When you hit 'L', you should append the (number+1) to the left of the current number.
When you hit 'R', you should append the (number+1) to the right of the current number.
"""


class Node():
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def func(s):
    n = len(s)
    head = headPtr = Node(1)
    res = []
    i = 0
    while i < n:
        print(s[i], i+2)
        new_node = Node(i+2)
        if s[i] == 'L':
            if headPtr.prev:
                temp = headPtr.prev
                temp.next = None
                new_node.prev = temp
                temp.next = new_node
                headPtr.prev = new_node
                new_node.next = headPtr
                headPtr = headPtr.prev
            else:
                new_node.next = headPtr
                headPtr.prev = new_node
                headPtr = headPtr.prev
                
            while head.prev:
                head = head.prev
                
        if s[i] == 'R':
            if headPtr.next:
                temp = headPtr.next
                new_node.next = temp
                temp.prev = new_node
                headPtr.next = new_node
                new_node.prev = headPtr
                headPtr = headPtr.next
            else:
                headPtr.next = new_node
                new_node.prev = headPtr
                headPtr = headPtr.next
        i += 1
            
    while head:
        res.append(head.val)
        head = head.next
    return res

print(func("LLRLRRL"))
