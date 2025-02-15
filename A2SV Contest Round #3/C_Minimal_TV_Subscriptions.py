from collections import defaultdict



for _ in range(int(input())):
    n, k, d = map(int, input().split())
    nums = list(map(int, input().split()))
    window = defaultdict(int)
    l = 0
    for _ in range(d):
        window[nums[_]] += 1
        if window[nums[_]] == 1:
            l += 1
    res = float("inf")
   
    left = 0
    for right in range(d, n):
        res = min(res, l)
        window[nums[right]] += 1
        
        if window[nums[right]] == 1:
            l += 1
        window[nums[left]] -= 1
        if window[nums[left]] == 0:
            l -= 1
        left += 1
        
        
    res = min(res, l)
        
            
    
       
    
      
    print(res)
        
    #print(res)