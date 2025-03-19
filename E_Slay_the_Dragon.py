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
total = sum(nums)

for _ in range(INT_INPUT()):
    x, y = TUPLE_INT_INPUT()
    
    index = min(n - 1, bisect_right(nums, x))
    
    left = max(0, index - 1)
    
    from_left = max(0, x - nums[left]) + max(y - (total - nums[left]), 0)
    
    from_right = max(0, x - nums[index]) + max(y -(total - nums[index]), 0)
    
    print(max(0, min(from_left, from_right)))