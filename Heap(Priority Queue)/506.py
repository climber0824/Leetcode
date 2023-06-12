class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [[-j, i] for i, j in enumerate(score)]
        heapq.heapify(heap)
        cnt = 0
        res = [0] * len(score)
        while heap:
            _, idx = heapq.heappop(heap)                                 
            if cnt == 0:
                res[idx] = "Gold Medal"
            elif cnt == 1:
                res[idx] = "Silver Medal"
            elif cnt == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(cnt + 1)
            cnt += 1
        return res
