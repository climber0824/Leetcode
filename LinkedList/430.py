"""
430. Flatten a Multilevel Doubly Linked List
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """ sol1
        if not head: return head
        p = head
        while p:
            if not p.child:
                p = p.next
                continue
            temp = p.child
            while temp.next:
                temp = temp.next
            temp.next = p.next
            if p.next != None:
                p.next.prev = temp
            p.next = p.child
            p.child.prev = p
            p.child = None
        
        return head
        """
        ### sol2
        if not head: return
        dummy = Node(0, None, head, None)
        stack = []
        stack.append(head)
        prev = dummy
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root

            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root
        dummy.next.prev = None

        return dummy.next
