class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        res = inf
        vis = set()
        q = deque([1])
        
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w

        while q:
            node = q.popleft()
            for adj, scr in graph[node].items():
                if adj not in vis:
                    vis.add(adj)
                    q.append(adj)
                res = min(res, scr)
        
        return res
