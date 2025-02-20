for _ in range(int(input())):
    n, x = map(int, input().split())
    
    nums = list(map(int, input().split()))
    
    nums.sort(reverse=True)
    
    total = 0
    l = 0
    for i in range(n):
        total += nums[i]
        if total / (i + 1) < x:
            break
        l = i + 1
        
    print(l)
        