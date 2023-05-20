class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
      g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def dfs(i):
            component.add(i)
            for nei in g[i]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        ans = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                component = set()
                seen.add(i)
                dfs(i)
                if all(len(g[node]) == len(component) - 1 for node in component):
                    ans += 1
        return ans
