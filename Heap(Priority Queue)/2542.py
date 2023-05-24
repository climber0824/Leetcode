class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # sorted by nums2 in decending order
        nums = sorted(zip(nums1, nums2), key=lambda f : -f[1])         
        heap = []
        res = 0
        total = 0

        for a, b in nums:
            heapq.heappush(heap, a)
            total += a
            # if length of heap bigger than k, pop the smallest from heap
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, total * b)
            
        return res
