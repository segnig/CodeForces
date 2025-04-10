from bisect import bisect_left
import sys, threading
def input():return sys.stdin.readline().strip()
def INT_INPUT():return int(input())
def TUPLE_INPUT():return input().split()
def TUPLE_INT_INPUT():return map(int, input().split())
def LIST_INT_INPUT():return list(map(int, input().split()))
def LIST_INPUT():return list(input().split())

def merge(half_left, half_right):
    merged = []
    
    left = 0
    right = 0
    while left < len(half_left) and right < len(half_right):
        if half_left[left] <= half_right[right]:
            merged

def mergesort(nums):
    if len(nums) == 1:
        return nums
    left = mergesort(nums[:len(nums)//2])
    right = mergesort(nums[len(nums)//2:])
    
    return merge(left, right)


for _ in range(INT_INPUT()):
    n = INT_INPUT()
    nums = LIST_INT_INPUT()
    
    result = sorted(nums)
    
    ans = [0] * (2**n)
    
    for _ in range(2**n):
        res = bisect_left(result, nums[_])
        ans[_] = res + nums[_]
    
    print(*ans)