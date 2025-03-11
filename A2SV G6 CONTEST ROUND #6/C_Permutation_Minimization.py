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

from collections import deque
for _ in range(INT_INPUT()):
    n = INT_INPUT()
    nums = LIST_INT_INPUT()
    
    result = deque()
    
    for num in nums:
        if not result:
            result.append(num)
        elif num < result[0]:
            result.appendleft(num)
        else:
            result.append(num)
    
    print(*result)