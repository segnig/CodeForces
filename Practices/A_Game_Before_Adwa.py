for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    
    left = 0
    right = n - 1
    result = 0
    
    while left < right:
        if nums[left] + nums[right] == k:
            result += 1
            left += 1
            right -= 1
        elif nums[left]+nums[right]>k:
            right-=1
        else:
            left+=1
    print(result)
        