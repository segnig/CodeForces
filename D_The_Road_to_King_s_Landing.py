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

def solver(nums, k):
    left = 0
    right = 0
    for l, r in nums:
        left = max(left - k, l)
        right = min(right + k, r)
        if left > right:
            return False
    return True
            
for _ in range(INT_INPUT()):
    nums = []
    max_num = 0
    for _ in range(INT_INPUT()):
        l, r = TUPLE_INT_INPUT()
        nums.append((l, r))
        max_num = max(max_num, r)
    
    right = max_num
    left = 0
    best = 0
    
    while left <= right:
        mid = (left + right) // 2
        if solver(nums, mid):
            best = mid
            right = mid - 1
        else:
            left = mid + 1
            
    print(left)