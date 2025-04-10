import sys, threading

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

from bisect import bisect_left
from collections import deque

n, k = TUPLE_INT_INPUT()

word = input()
result = n - 1

left, right = 0, 0
store = deque()

while right < n:
    if word[right] == "0":
        store.append(right)
    if len(store) == k + 1:
        l, r = store[0], store[-1]
        mid = (r + l) // 2
        p = bisect_left(store, mid)
        result = min(result, max(store[p-1] - l, r - store[p-1]))
        result = min(result, max(store[p] - l, r - store[p]))
        
        store.popleft()
    right += 1

print(result)