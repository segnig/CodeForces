import math
import sys, threading
def input():return sys.stdin.readline().strip()
def INT_INPUT():return int(input())
def TUPLE_INPUT():return input().split()
def TUPLE_INT_INPUT():return map(int, input().split())
def LIST_INT_INPUT():return list(map(int, input().split()))
def LIST_INPUT():return list(input().split())

def is_possible(demands, hours, k, mid):
    taken = 0
    for i in range(len(demands)):
        taken += (math.ceil(demands[i] / mid) * hours[i])
    return taken <= k
    

for _  in range(INT_INPUT()):
    n, k = TUPLE_INT_INPUT()
    demands= LIST_INT_INPUT()
    hours = LIST_INT_INPUT()
    
    if k < sum(hours):
        print(-1)
    else:
        left = 1
        right = max(demands)
        while left <= right:
            mid = left + (right - left) // 2
            if is_possible(demands=demands, hours=hours, k=k, mid=mid):
                right = mid - 1
            else:
                left = mid + 1
        print(left)
        