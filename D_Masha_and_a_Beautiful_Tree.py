import sys
def input():return sys.stdin.readline().strip()
def INT_INPUT():return int(input())
def TUPLE_INPUT():return input().split()
def TUPLE_INT_INPUT():return map(int, input().split())
def LIST_INT_INPUT():return list(map(int, input().split()))
def LIST_INPUT():return list(input().split())

def merge_sort(nums):
    global result
    if len(nums) == 1:
        return nums
    left = merge_sort(nums=nums[:len(nums) // 2])
    right = merge_sort(nums=nums[len(nums)//2:])
    return merge(left, right)
    
    
def merge(left_half, right_half):
    global result
    if left_half[0] > right_half[0]:
        result += 1
        return right_half + left_half
    else:
        return left_half + right_half

for _ in range(INT_INPUT()):
    INT_INPUT()
    nums = LIST_INT_INPUT()
    result = 0
    if sorted(nums) == merge_sort(nums=nums):
        print(result)
    else:
        print(-1)