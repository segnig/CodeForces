from collections import defaultdict


n, m = map(int, input().split())

degree = [0] * n

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    degree[a-1] += 1
    degree[b-1] += 1

if m > n:
    print("unknown topology")

elif n == m:
    if degree.count(2) == m:
        print("ring topology")
    else:
        print("unknown topology")

elif n == m +1:
    if 1 == degree.count(m) and degree.count(1) == m:
        print("star topology")
    elif degree.count(1) == 2:
        print("bus topology")
    else:
        print("unknown topology")
else:
    print("unknown topology")