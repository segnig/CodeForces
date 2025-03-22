from collections import Counter
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
    n, k = TUPLE_INT_INPUT()
    
    nums = LIST_INT_INPUT()
    sorted_nums = [k - x % k for x in nums if x % k]
    sorted_nums.sort()
    
    counter = Counter(sorted_nums)
    
    result = [1 + key + ((val - 1)* (k)) for key, val in counter.items()]
    
    if result:
        print(max(result))
    else:
        print(0)
    