from math import inf
import math
import sys, threading
def input():return sys.stdin.readline().strip()
def INT_INPUT():return int(input())
def TUPLE_INPUT():return input().split()
def TUPLE_INT_INPUT():return map(int, input().split())
def LIST_INT_INPUT():return list(map(int, input().split()))
def LIST_INPUT():return list(input().split())

for _ in range(INT_INPUT()):
    n = INT_INPUT()
    hours = LIST_INT_INPUT()
    power = LIST_INT_INPUT()
    
    stack = [[inf, power[0]]]
    result = 0
    
    for i in range(1, n):
        hour = hours[i]
        count = 0
        while hour > 0:
            taken = math.ceil(hour /stack[-1][1])
            if taken > stack[-1][0]:
                hour -= stack[-1][0] * stack[-1][1]
                count += stack[-1][0]
                stack.pop()
            else:
                stack[-1][0] -= taken
                count += taken
                hour = 0
        stack.append([count, power[i]])
        result = max(result, count)          
    print(result)
    