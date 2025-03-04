import sys

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

for _ in range(INT_INPUT()):
    input()
    n, k = TUPLE_INT_INPUT()
    
    tem = [float("inf")] * n
    inds = LIST_INT_INPUT()
    
    values = LIST_INT_INPUT()
    
    for i in range(k):
        tem[inds[i] - 1] = values[i]
        
    before = float("inf")
    for i in range(n -1, -1, -1):
        before = min(before, tem[i])
        tem[i] = before
        before += 1
        
    before = float("inf")
    for i in range(n):
        before = min(before, tem[i])
        tem[i] = before
        before += 1
    print(*tem)