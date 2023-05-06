"""
Given : string including 'L' and 'R'
Return: array of nums

When you hit 'L', you should append the (number+1) to the left of the current number.
When you hit 'R', you should append the (number+1) to the right of the current number.

func : using double linkedlist
func2: using deque
"""
from collections import deque

class Node():
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class solution():
    
    def func(self, s):
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


    def func2(self, s):
        n = len(s)
        num = n
        dq = deque([num + 1])
        num -= 1
        while num >= 0:
            if s[num] == 'R':
                dq.appendleft(num + 1)
            else:
                dq.append(num + 1)
            num -= 1

        return list(dq)

    
if __name__ == "__main__":
    sol = solutions()
    print(sol.func("LLRLRRL"))
    print(sol.func2("LLRLRRL"))
