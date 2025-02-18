n, k, q = map(int, input().split())

prefix = [0 for i in range(200002)]

for i in range(n):
    x, y = map(int, input().split())
    prefix[x] += 1
    prefix[y + 1] -= 1

for i in range(1, 200002):
    prefix[i] += prefix[i - 1]
    
for i in range(len(prefix)):
    if prefix[i] >= k:
        prefix[i] = 1
    else:
        prefix[i] = 0

for i in range(1, 200002):
    prefix[i] += prefix[i - 1]
    
for _ in range(q):
    a, b = map(int, input().split()) 
    print(prefix[b] - prefix[a - 1])