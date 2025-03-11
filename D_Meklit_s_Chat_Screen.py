from collections import deque
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

n, k = TUPLE_INT_INPUT()

ids = LIST_INT_INPUT()

on_screen = set()
result = deque()

for id in ids:
    if k > len(result):
        if id not in on_screen:
            result.appendleft(id)
            on_screen.add(id)
    else:
        if id not in on_screen:
            popped = result.pop()
            on_screen.remove(popped)
            result.appendleft(id)
            on_screen.add(id)
print(len(result))
print(*result)
        