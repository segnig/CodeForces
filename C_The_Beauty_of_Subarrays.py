import sys

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
    n = INT_INPUT()
    
    nums = LIST_INT_INPUT()
    
    result = ["1"]
    missed = 0
    index = nums.index(1)
    left = index - 1
    right = index + 1
    max_n = 1
    
    while left > -1 and right < n:
        if nums[left] < nums[right]:
            if nums[left] < max_n:
                missed -= 1
            else:
                missed += nums[left] - len(result) - 1
            left -= 1
            if missed == 0:
                result.append("1")
            else:
                result.append("0")
            max_n = max(max_n, nums[left+1])
        else:
            if nums[right] < max_n:
                missed -= 1
            else:
                missed += nums[right] - len(result) - 1
            right += 1
            if missed == 0:
                result.append("1")
            else:
                result.append("0")
            max_n = max(max_n, nums[right - 1])
        
    while left > -1:
        if nums[left] < max_n:
                missed -= 1
        else:
            missed += nums[left] - len(result) - 1
        left -= 1
        if missed == 0:
            result.append("1")
        else:
            result.append("0")
        max_n = max(max_n, nums[left + 1])
            
        
    
    while right < n:
        if nums[right] < max_n:
                missed -= 1
        else:
            missed += nums[right] - len(result) - 1
        right += 1
        if missed == 0:
            result.append("1")
        else:
            result.append("0")
        max_n = max(max_n, nums[right - 1])
        
            
    print("".join(result))