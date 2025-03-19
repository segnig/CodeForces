from math import *

t = int(input())

for _ in range(t):
    s = input()
    input()
    arr = [int(i) for i in input().split()]
    result = []
    
    def solve(k):
        if k <= len(s):
            return s[k-1]
        curr_level = ceil(log2(ceil(k/len(s))))
        prev = 2**(curr_level - 1) * len(s)
        k = k - prev 
        return solve(k).swapcase()
        
    
    for k in arr:
        result.append(solve(k))
    print(*result)