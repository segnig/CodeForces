import sys, threading
def input():return sys.stdin.readline().strip()
def INT_INPUT():return int(input())
def TUPLE_INPUT():return input().split()
def TUPLE_INT_INPUT():return map(int, input().split())
def LIST_INT_INPUT():return list(map(int, input().split()))
def LIST_INPUT():return list(input().split())
from bisect import *

for _ in range(INT_INPUT()):
    n, q = TUPLE_INT_INPUT()
    nums = LIST_INT_INPUT()
    queries = []
    for _ in range(q):
        k, x = TUPLE_INT_INPUT()
        queries.append((k, x, _))
    queries.sort()
    result = [0] * q
    
    store = []
    for h in queries:
        
        for i in range(len(store), h[0], 1):
            insort(store, nums[i])
        res = bisect_left(store, h[1])
        result[h[2]] = res
    
    for r in result:
        print(r)
    