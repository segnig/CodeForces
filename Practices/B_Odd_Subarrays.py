for _ in range(int(input())):
    n = int(input())
    
    nums = list(map(int,  input().split()))
    
    diff = [
        nums[i] - nums[i-1] for i in range(1, n)
    ]
    res = 0
    left = 0
    while left < n - 1:
        if diff[left] < 0:
            res += 1
            left += 1
        left += 1
    
    print(res)
    