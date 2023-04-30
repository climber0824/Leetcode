class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY: return 0
            root[rootX] = rootY
            return 1
        
        res = e1 = e2 = 0
        root = [i for i in range(n+1)]        
        
        # Alice and Bob
        for t, i, j in edges:
            if t == 3:
                if union(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        root0 = root[:]        

        # only Alice
        for t, i, j in edges:
            if t == 1:
                if union(i, j):
                    e1 += 1
                else:
                    res += 1        

        # only Bob
        root = root0
        for t, i, j in edges:
            if t == 2:
                if union(i, j):
                    e2 += 1
                else:
                    res += 1
        return res if e1 == e2 == n - 1 else -1
