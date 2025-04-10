from bisect import bisect_right

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

n = INT_INPUT()
nums = LIST_INT_INPUT()
nums.sort()

for _ in range(INT_INPUT()):
    index = bisect_right(nums, INT_INPUT())
    if index == -1:
        print(0)
    else:
        print(index)