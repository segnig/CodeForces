from collections import defaultdict


class UnionFind:
    def __init__(self, n, gov):
        self.parent = [i  for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
        
        self.gov = gov
        
        
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
    
        return self.parent[x]
    
    def union(self, u, v):
        p_u = self.find(u)
        p_v = self.find(v)
        
        if (p_u == p_v) or ((p_v in  self.gov) and (p_u in self.gov)):
            return 0
        if p_v in self.gov:
            self.parent[p_u] = p_v
            self.size[p_v] += self.size[p_u]
            return self.size[p_u]
        
        elif p_u in self.gov:
            self.parent[p_v] = p_u
            self.size[p_u] += self.size[p_v]
            return self.size[p_v]
        
        elif self.size[p_u] > self.size[p_v]:
            self.parent[p_u] = p_v
            self.size[p_v] += self.size[p_u]
            return 0
        else:
            self.parent[p_v] = p_u
            self.size[p_u] += self.size[p_v]
            return 0
            

n, m, k = map(int, input().split())

gov = set(list(map(int, input().split())))

graph = defaultdict(list)

uf = UnionFind(n=n, gov=gov)

for _ in range(int(m)):
    u, v = map(int, input().split())
    uf.union(u, v)
    
big_num = None
p = 0
for k in gov:
    if uf.parent[k] > p:
        big_num = k
        p = uf.parent[k]

count = 0
print(big_num)
for i in range(1, n+1):
    par = uf.find(i)
    if par not in gov:
        count += uf.size[par] * uf.parent[big_num]
        uf.union(big_num, par)
    print(i, count)
        
        
    
print(count)
    