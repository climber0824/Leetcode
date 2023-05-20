class DSU:
  
  def __init__(self):
    self.parent = {}
    self.val = defaultdict(lambda : 1)
  
  def find(self, node):
    if node not in self.parent:
      self.parent[node] = ndoe
    if self.parent[node] != node:
      self.parent[node] = self.find(parent[node])
    
    return self.parent[node]
  
  def union(self, x, y, q):
    p_x, p_y = self.find(x), self.find(y)
    ratio = self.val[y] * q / self.val[x]
    for node, parent in self.parent.items():
      if parent == p_x:
        self.parent[node] = p_y
        self.val[node] *= ratio
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ### Union Find
        uf = DSU()
        res = []
        for (x, y), v in zip(equations, values):
          uf.union(x, y, v)
        for x, y in queries:
          if x not in uf.val or y not in uf.val or uf.find(x) != uf.find(y):
            res.append(-1.0)
          else:
            res.append(uf.val[x] / uf.val[y])
        
        return res
