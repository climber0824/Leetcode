class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return 0
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        return 1


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        n = len(nums)
        uf = DSU(n)
        
		# TO FIND PRIME FACTORS
        def getPrimeDivs(n):
            if n < 0: return []
            res = set()

            for i in range(2, isqrt(n) + 1):
                while n % i == 0:
                    res.add(i)
                    n //= i

            if n > 1: res.add(n)
            return res
        
        primes = defaultdict(list) # Stores the indices of elements having key as a prime factor
        for idx, i in enumerate(nums):
            primeDivs = getPrimeDivs(i)
            
            for p in primeDivs:
                primes[p].append(idx)
        
		# UNITE INDICES HAVING SAME PRIME FACTORS
        for p in primes:
            for i in primes[p]:
                uf.union(i, primes[p][0])
        
		# CHECK IF THE GRAPH IS CONNECTED
        return sum(i == uf.find(i) for i in range(n)) == 1
