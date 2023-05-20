class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]], mode: int) -> List[float]:
      if mode:
        self.DFS(equations, values, queries)
      else:
        self.BFS(equations, values, queries)
    
    def BFS(self, equations, values, queries):
      graph = defaultdict(dict)
        for ([x, y], value) in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1 / value
        
        def bfs(s, e):
            if s not in graph or e not in graph:
                return -1.0
            if s == e:
                return 1.0
            q = deque([(s, 1.0)])
            visited = {s}
            while q:
                node, curr = q.popleft()
                for child, value in graph[node].items():
                    if child in visited:
                        continue
                    curr_product = curr * value
                    if child == e:
                        return curr_product
                    graph[s][child] = curr_product
                    graph[child][s] = 1 / curr_product
                    visited.add(child)
                    q.append((child, curr_product))
            return -1
        return [bfs(s, e) for (s, e) in queries]
      
    def DFS(self, equations, values, queries):
      g = defaultdict(dict)
        res = []
        for (u, v), val in zip(equations, values):
            g[u][v] = val
            g[v][u] = 1.0 / val
        
        def dfs(x, y, seen):
            if x not in g or y not in g:
                return -1.0
            if y in g[x]:
                return g[x][y]
            for nei in g[x]:
                if nei not in seen:
                    seen.add(nei)
                    temp = dfs(nei, y, seen)
                    if temp == -1:
                        continue
                    else:
                        return temp * g[x][nei]
            return -1
        
        for u, v in queries:
            res.append(dfs(u, v, set()))

        return res

if __name__ == "__main__":
  sol = Solution()
  bfs = false
  dfs = true
  if bfs:
    return sol.calcEquation(equations, values, queries, 0)
  if dfs:
    return sol.calcEquation(equations, values, queries, 1)
     
