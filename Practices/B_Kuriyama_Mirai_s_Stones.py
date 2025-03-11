import sys

def input():
    return sys.stdin.readline().strip()

def INT_INPUT():
    return int(input())


def TUPLE_INT_INPUT():
    return map(int, input().split())

def LIST_INT_INPUT():
    return list(map(int, input().split()))

def prefix_sum(nums):
    pref = [0]
    for i in range(len(nums)):
        pref.append(pref[-1] + nums[i])
    return pref


input()

nums = LIST_INT_INPUT()
sorted_nums = sorted(nums)

nums = prefix_sum(nums)
sorted_nums = prefix_sum(sorted_nums)

for _ in range(INT_INPUT()):
    type, l, r = TUPLE_INT_INPUT()
    
    if type == 1:
        print(nums[r] - nums[l - 1])
    else:
        print(sorted_nums[r] - sorted_nums[l - 1])
        