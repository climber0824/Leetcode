class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [1] * N
    
    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        
        return self.parent[p]

    def union(self, p, q):
        p_root, q_root = self.find(p), self.find(q)
        if p_root == q_root: return False
        if self.rank[p_root] > self.rank[q_root]:
            p_root, q_root = q_root, p_root
        self.parent[p_root] = q_root
        self.rank[q_root] += self.rank[p_root]

        return True 

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, u, v) for u, v, w in edgeList)
        uf = UnionFind(n)
        ans = [None] * len(queries)
        idx = 0

        for w, p, q, i in queries:
            while idx < len(edgeList) and edgeList[idx][0] < w:
                _, u, v = edgeList[idx]
                uf.union(u,v)
                idx += 1
            ans[i] = uf.find(p) == uf.find(q)
        
        return ans
