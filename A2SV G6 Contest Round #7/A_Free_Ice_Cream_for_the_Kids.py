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


n, x = TUPLE_INT_INPUT()

count = 0
for _ in range(n):
    op, xi = TUPLE_INPUT()
    xi = int(xi)
    
    if op == "-":
        if x < xi:
            count += 1
        else:
            x -= xi
    else:
        x += xi
print(x, count)
            