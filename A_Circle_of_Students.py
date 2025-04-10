for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    result = []
    
    for i in range(1, n):
        result.append(abs(nums[i] - nums[i-1]))
    result.append(abs(nums[0] - nums[-1]))
    
    c = result.count(1)
    
    if c >= n -1:
        print("YES")
    else:
        print("NO")