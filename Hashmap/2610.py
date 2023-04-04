class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        seen = set()
        res = []        
        
        while cnt:
            seen = set(cnt)
            res.append(list(seen))
            for i in list(seen):
                cnt[i] -= 1
                if cnt[i] == 0:
                    del cnt[i]                
            
        return res
