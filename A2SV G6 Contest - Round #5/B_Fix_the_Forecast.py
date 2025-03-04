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
    n, k = TUPLE_INT_INPUT()
    a = LIST_INT_INPUT()
    b = LIST_INT_INPUT()
    
    b.sort()
    
    ind_val_a = {}
    a_copy = [(val, i) for i, val in enumerate(a)]
    
    a_copy.sort()
    result = [0] * n
    
    for i in range(n):
        result[a_copy[i][1]] = b[i]
        
    print(*result)