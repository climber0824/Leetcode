class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        prev = curr = head
        dummy = head
        curr = curr.next
        while prev and curr:            
            while curr and curr.val == prev.val:
                curr = curr.next
            prev.next = curr
            prev = prev.next
            
        return dummy
