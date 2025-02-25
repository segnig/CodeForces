for _ in range(int(input())):
    nums = list(map(int, input().split()))
    mx = max(nums)
    result = []
    
    for num in nums:
        if nums.count(mx) == 3:
            result.append(1)
        elif nums.count(mx) == 1 and num == mx:
            result.append(0)
        elif nums.count(mx) == 2 and num == mx:
            result.append(1)
        elif nums.count(mx) == 2 and num != mx:
            result.append(mx - num + 1)
        else:
            if num == mx:
                result.append(0)
            else:
                result.append(mx - num + 1)
                
    print(*result)