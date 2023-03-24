class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        def dfs(i, par):
            res = 0
            for j in out_graph[i]:
                if j == par:
                    continue
                res += 1
                res += dfs(j, i)
            for j in in_graph[i]:
                if j == par:
                    continue
                res += dfs(j, i)
            return res

        in_graph = [[] for _ in range(n)]
        out_graph = [[] for _ in range(n)]
        for u, v in connections:
            out_graph[u].append(v)
            in_graph[v].append(u)
        
        return dfs(0, -1)
        """
        """
        self.res = 0    
        roads = set()
        graph = collections.defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)

        def dfs(u, parent):            
            self.res += (parent, u) in roads # True or False
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)    
        dfs(0, -1)
        return self.res
        """
        g = defaultdict(list)
        for u, v in connections:
            g[u].append((v, 1))
            g[v].append((u, 0))

        q = deque([0])
        seen = {0}
        res = 0        
        
        while q:
            node = q.popleft()
            for nei, cost in g[node]:
                if nei not in seen:
                    seen.add(nei)                    
                    res += cost
                    q.append(nei)
        return res
