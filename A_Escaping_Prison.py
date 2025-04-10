import sys, threading
def input():return sys.stdin.readline().strip()
def INT_INPUT():return int(input())
def TUPLE_INPUT():return input().split()
def TUPLE_INT_INPUT():return map(int, input().split())
def LIST_INT_INPUT():return list(map(int, input().split()))
def LIST_INPUT():return list(input().split())

for _ in range(INT_INPUT()):
    n, h = TUPLE_INT_INPUT()
    res = 0
    for _ in range(n):
        res += max(TUPLE_INT_INPUT())
    
    if h <= res:
        print("YES")
    else:
        print("NO")