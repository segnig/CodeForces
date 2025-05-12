from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return self.parent[x]

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        u_p = self.find(u)
        v_p = self.find(v)

        if u_p != v_p:
            if self.size[u_p] > self.size[v_p]:
                self.parent[v_p] = u_p
                self.size[u_p] += self.size[v_p]  
            else:
                self.parent[u_p] = v_p
                self.size[v_p] += self.size[u_p] 



n,k = map(int, input().split())

uf = UnionFind(n+1)

stores = set()

counter = Counter()

for _ in range(k):
    pair = list(map(int, input().split()))
    
    if tuple(sorted(pair)) not in stores:
        counter[pair[0]] += 1
        counter[pair[1]] += 1
    stores.add(tuple(sorted(pair)))
    
result = k - len(stores)

stores = list(stores)

stores.sort(key=lambda x:counter[x[1]] + counter[x[0]], reverse=True)



for a, b in stores:
    a_p = uf.find(a)
    b_p = uf.find(b)
    
    if a_p == b_p:
        result += 1
        
    uf.union(a, b)

print(result)