class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        def dfs(g, node, seen, res):
            seen[node] = True
            for nei in g[node]:
                if not seen[nei]:
                    dfs(g, nei, seen, res)
                elif nei in res: # nei can be visited by current vertex so we dont have to add nei in res
                    res.remove(nei)

        g = defaultdict(list)
        seen = [False] * n
        res = set()   
        self.count = 0    
        for u, v in edges:
            g[u].append(v)
        
        for i in range(n):
            if not seen[i]:
                dfs(g, i, seen, res)
                res.add(i)  # add vertex from which we start traversing
                
        return res
