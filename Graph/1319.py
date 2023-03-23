class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """ dfs
        if len(connections) < n - 1: return -1        
        graph = defaultdict(list)
        conn = 0
        seen = [0] * n
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)        
        
        def dfs(node):
            if seen[node] == 1:
                return 0
            seen[node] = 1
            for nei in graph[node]:
                dfs(nei)
            return 1

        
        return sum(dfs(i) for i in range(n)) - 1
        """
        """
        # union find
        self.id, self.count = list(range(n)), n
        
        def union(x, y):
            
            def find(x):
                while x != self.id[x]:
                    x = self.id[x]
                return x
            
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            self.id[rx] = ry
            self.count -= 1
        
        for u, v in connections:
            union(u, v)
        
        return -1 if len(connections) < n - 1 else self.count - 1
        """
        # bfs
        if len(connections) < n - 1: return -1
        g = defaultdict(list)
        seen = set()
        count = 0

        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        def bfs(node):
            seen.add(node)
            q = deque([node])
            while q:
                n = q.popleft()
                for nei in g[n]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
        
        for i in range(n):
            if i not in seen:
                count += 1
                bfs(i)
        
        return count - 1
