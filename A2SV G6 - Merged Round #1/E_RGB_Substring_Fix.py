from math import ceil
import sys

def input():
    return sys.stdin.readline().strip()

def INT_INPUT():
    return int(input())

def TUPLE_INT_INPUT():
    return map(int, input().split())

def LIST_INT_INPUT():
    return list(map(int, input().split()))

for _ in range(INT_INPUT()):
    n, k = TUPLE_INT_INPUT()
    word = input()
    
    R = "RGB" * ceil(n / 3)
    B = "BRG" * ceil(n / 3)
    G = "GBR" * ceil(n / 3)
    
    R = R[:n]
    B = B[:n]
    G = G[:n]
    
    G_nums = [0] * n
    R_nums = [0] * n
    B_nums = [0] * n
    
    for i in range(n):
        G_nums[i] = word[i] != G[i]
        R_nums[i] = word[i] != R[i]
        B_nums[i] = word[i] != B[i] 
    
    r_sum, b_sum, g_sum = 0, 0, 0
    result = k
    
    for i in range(k):
        r_sum += R_nums[i]
        b_sum += B_nums[i]
        g_sum += G_nums[i]
        
    result = min(result, r_sum, b_sum, g_sum)
    
    for i in range(k, n):
        r_sum += R_nums[i] - R_nums[i - k]
        b_sum += B_nums[i] - B_nums[i - k]
        g_sum += G_nums[i] - G_nums[i - k]
        
        result = min(result, r_sum, b_sum, g_sum)
    
    print(result)