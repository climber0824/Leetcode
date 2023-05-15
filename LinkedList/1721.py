# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast, dummy = head, head, head
        num_1, num_2 = 0, 0
        tmp_k = k
        
        while k - 1 != 0:
            fast = fast.next
            k -= 1
        num_1 = fast.val
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        num_2 = slow.val
        slow.val = num_1
        
        while dummy:
            tmp_k -= 1
            if tmp_k == 0:
                dummy.val = num_2
                break
            dummy = dummy.next
        return head
