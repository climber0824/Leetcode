#725. Split Linked List in Parts
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        prev, curr = None, head
        total = 0
        res = [None] * k
        while curr:
            total += 1
            curr = curr.next
        curr = head
        size, remaining = divmod(total, k)
    
        for i in range(k):
            res[i] = curr
            for j in range(size + int(remaining > 0)):
                prev = curr
                curr = curr.next
            if prev:
                prev.next = None
            remaining -= 1

        return res
