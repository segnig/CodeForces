import sys
from collections import defaultdict

def INT_INPUT():
    return int(input())

def TUPLE_INT_INPUT():
    return map(int, input().split())



n = INT_INPUT()
events = defaultdict(int)

for _ in range(n):
    l, r = TUPLE_INT_INPUT()
    events[l] += 1
    events[r + 1] -= 1

keys = sorted(events.keys())
coverage = 0
prev = keys[0]
result = defaultdict(int)


for point in keys:
    result[coverage] += point - prev
    coverage += events[point]
    prev = point

ans = [result[k] for k in range(1, n + 1)]
print(*ans)