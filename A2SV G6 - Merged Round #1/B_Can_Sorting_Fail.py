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

for _ in range(INT_INPUT()):
    n = INT_INPUT()
    nums = LIST_INT_INPUT()
    sorted_nums = sorted(nums)
    
    if nums == sorted_nums:
        print("NO")
    else:
        print("YES")