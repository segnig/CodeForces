import sys, threading
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().strip()

def INT_INPUT():
    return int(input())

def TUPLE_INPUT():
    return input().split()

def TUPLE_INT_INPUT():
    return map(int, input().split())

def LIST_INT_INPUT():
    return list(map(int, input().split()))

def LIST_INPUT():
    return list(input().split())

n, b = TUPLE_INT_INPUT()
nums = LIST_INT_INPUT()

store = []
for _ in range(b):
    a, c = TUPLE_INT_INPUT()
    store.append([a, c])
    
store.sort(key=lambda x: x[0])
prev = 0
for i in range(b):
    store[i][1] += prev
    prev = store[i][1]
    
result = []

bs = [ store[i][0] for i in range(b) ]
for i in range(n):
    idx = bisect_right(bs, nums[i])
    if idx == 0:
        result.append(0)
    else:
        result.append(store[idx - 1][1])

print(*result)