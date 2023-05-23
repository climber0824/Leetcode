class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
      # using max_heap
      max_heap = []
      projects = sorted(zip(profits, capital), key=lambda x : x[1])
      i = 0
      for _ in range(k):
        # if capital less than curr w and i less than len(profits)
        while i < len(profits) and projects[i][1] <= w:
          # push the profits into max_heap
          heapq.heappush(max_heap, -projects[i][0])
          i += 1
        if max_heap:
          w -= heapq.heappop(max_heap)
        else:
          break
       return w
