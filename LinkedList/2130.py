# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:        
        slow = head
        fast = head
        res = 0
        
        # find half of the linkedlist
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None

        # reverse the front half of the linkedlist
        dummy = head
        prev = None
        curr = dummy
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # add the reversed front linkedlist and the back of the linkedlist
        while prev:
            res = max(res, prev.val + temp.val)
            prev = prev.next
            temp = temp.next

        return res

        """
        # time : O(n) + O(n)
        # space : O(n)
        
        arr = []
        size = 0
        while head:
            arr.append(head.val)
            size += 1
            head = head.next
        l, r = 0, size - 1
        res = 0
        while l < r:
            res = max(res, arr[l] + arr[r])
            l += 1
            r -= 1
    
        return res
        """
