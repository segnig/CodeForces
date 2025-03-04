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

n, t, c = TUPLE_INT_INPUT()

nums = LIST_INT_INPUT()

numbers = []

sub = []
for num in nums:
    if num > t:
        numbers.append(sub)
        sub = []
    else:
        sub.append(num)
numbers.append(sub)

result = 0

for nums in numbers:
    
    if len(nums) >= c:
        result += len(nums) - c + 1
print(result)

