class DSU:
    def __init__(self, nums):
        self.parent = {i: i for i in nums}
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
        
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # UF_2
        if not nums: return 0
        uf = DSU(nums)
        
        S = set(nums)
        for n in S:
            if n - 1 in S:
                uf.union(n, n-1)        
        C = Counter()
        for n in S:
            C[uf.find(n)] += 1
        
        return max(C.values())
        """ UF_1
        if not nums:
            return 0
        
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        S = set(nums)
        
        for n in S:
            union(n,n)
            if n+1 in S:
                union(n+1,n)
        
        # find lengths of all the sequences
        c = Counter()
        """
