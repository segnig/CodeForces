import sys

def input():
    return sys.stdin.readline().strip()

def INT_INPUT():
    return int(input())

def TUPLE_INPUT():
    return input().split()



def LIST_INT_INPUT():
    return list(map(int, input().split()))

def prefix_sum(nums):
    pref = [0]
    for i in range(len(nums)):
        pref.append(pref[-1] + nums[i])
    return pref

for _ in range(INT_INPUT()):
    input()
    
    nums_a = LIST_INT_INPUT()
    input()
    nums_b = LIST_INT_INPUT()
    
    nums_a = prefix_sum(nums_a)
    nums_b = prefix_sum(nums_b)
    
    print(max(nums_b) + max(nums_a))
    