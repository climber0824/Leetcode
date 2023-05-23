class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
      heap = []
      m, n = len(nums1), len(nums2)
      heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
      seen = set()
      set.add((0, 0)    
      res = []
              
      while len(res) < k and heap:
        _, i, j = heapq.heappop(heap)
        res.append([i, j])
        if i + 1 < m and (i+1, j) not in seen:
              heapq.heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
              seen.add((i+1, j))
        if j + 1 < n and (i, j+1) not in seen:
              heapq.heappush(heap, (nums1[i ] + nums2[j+1], i, j + 1))
              seen.add((i, j+1))
      return res
        
                   
