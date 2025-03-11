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
    n, l, r = TUPLE_INT_INPUT()
    
    nums = LIST_INT_INPUT()
    
    result = sum(sorted(nums[:r])[:r-l+1])
    
    result = min(
        result, 
        sum(sorted(nums[l-1:])[:r-l+1])
    )
    
    print(result)