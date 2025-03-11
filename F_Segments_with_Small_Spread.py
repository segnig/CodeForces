from collections import deque
import sys, threading
from heapq import *

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

nums = LIST_INT_INPUT()

increase = deque([0])
decrease = deque([0])
left = -1

result = 0

for right in range(n):
    while increase and nums[increase[-1]] < nums[right]:
        increase.pop()
    increase.append(right)
    while decrease and nums[decrease[-1]] > nums[right]:
        decrease.pop()
    decrease.append(right)
    while increase and abs(nums[increase[0]] - nums[right]) > k:
        left = max(left, increase.popleft())
    while decrease and abs(nums[decrease[0]] - nums[right]) > k:
        left = max(left, decrease.popleft())
        
    result += right - left
    
print(result)
        