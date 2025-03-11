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



def solve(nums):
    pref = [0]
    stack = []     
    for num in nums:
        pref.append(num + pref[-1])
    
    for i , num in enumerate(nums):
        while stack and num >= nums[stack[-1]]:
            k = stack.pop()
            sm = pref[i] - pref[k]
            if sm > 0:
                return False
        stack.append(i)
    return True
    

for _ in range(INT_INPUT()):
    n = INT_INPUT()
    nums = LIST_INT_INPUT()
    if solve(nums) and solve(nums=nums[::-1]):
        print("YES")
    else:
        print("NO")