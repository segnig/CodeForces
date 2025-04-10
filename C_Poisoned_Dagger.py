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

def solver(nums, k, h):
    res = 0
    for i in range(len(nums)):
        if i == len(nums) - 1:
            res += k
        else:
            res += min(nums[i + 1] - nums[i], k)
    
    return res >= h

for _ in range(INT_INPUT()):
    n, h = TUPLE_INT_INPUT()
    nums = LIST_INT_INPUT()

    nums.sort()

    left = 0
    right = h
    
    while left <= right:
        mid = (left + right) // 2
        if solver(nums, mid, h):
            right = mid - 1
        else:
            left = mid + 1
    print(left)