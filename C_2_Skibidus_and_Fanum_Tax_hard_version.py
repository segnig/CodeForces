from bisect import bisect_left
from math import inf

def solve():
    n, m = map(int, input().split())
    nums_a = list(map(int, input().split()))
    nums_b = list(map(int, input().split()))
    
    nums_b.sort()
    nums_a = [-inf] + nums_a
    
    
    for i in range(1, n+1):
        left = bisect_left(nums_b, nums_a[i] + nums_a[i-1])
        
        if left < m and nums_a[i] != nums_a[i-1]:
            value = nums_b[left] - nums_a[i]
            
            if value >= nums_a[i-1]:
                
                if nums_a[i] > nums_a[i-1]:
                    nums_a[i] = min(nums_a[i], value)
                else:
                    nums_a[i] = value
        if nums_a[i] < nums_a[i-1]:
            print("NO")
            return

    
    print("YES")

for _ in range(int(input())):
    solve()
