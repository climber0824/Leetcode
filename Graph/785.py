class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        using_BFS = False
        using_DFS = False
        using_UF = False
        
        if using_BFS:
          return BFS(graph)
        elif using_DFS:
          return DFS(graph)
        else:
          return UnionFind(graph)
       
      
    def BFS(graph):
        n = len(graph)
        color = [0] * n
        seen = set()
        q = deque()
    
        for i in range(n):
            if i not in seen:
                seen.add(i)
                color[i] = 1
                q.append(i)
            
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
                        color[nei] = color[node] ^ 1
                    else:
                        if color[nei] == color[node]:
                            return False
        return True
      
    def DFS(graph):     
      # DFS
        # A bipartite graph can be colored by using only two colors
        # where no neighboring/adjacent nodes share the same color

        n = len(graph)
        color = [0] * n
        
        def dfs(node):
            # we use DFS to traverse the nodes and assign them colors
			# if we come across a pair of neighbor/adjacent nodes that   share the same color, we return False
            for nei in graph[node]:
                if color[nei] == 0:
                    color[nei] = color[node] * -1
                    if not dfs(nei):
                        return False   
                else:
                    # if the neighbor node has already been visited, and,
                    # if color_of_current_node ==  color_of_neighbor_node
                    # it cannot be a bipartite graph
                    if color[nei] == color[node]:
                        return False
            return True

         # we loop through all unvisited nodes so that no node is left unprocessed
        # this is [IMPORTANT] because it's stated in the problem that - 
        # "The graph MAY NOT be connected, meaning there MAY BE two nodes u and v such that there is no path between them"
        for i in range(n):
            if color[i] == 0:
                color[i] = 1
                if not dfs(i):
                    return False
        return True  
      
    def UnionFind(graph):
        
        # Union find
        n = len(graph) 
        parent = [i for i in range(n)]
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent_x, parent_y = find(x), find(y)
            if parent_x != parent_y:
                parent[parent_x] = parent_y
        
        for i in range(n):
            parent_i = find(i)
            for j in graph[i]:
                if find(j) == parent_i:
                    return False
                union(graph[i][0], j)
        return True       
