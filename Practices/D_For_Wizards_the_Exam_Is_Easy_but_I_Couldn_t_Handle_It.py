for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    sorted_nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if sorted_nums[left] == nums[left]:
            left += 1
        elif sorted_nums[right] == nums[right]:
            right -= 1
        else:
            break
    
    if left == right:
        print(len(nums) - 1, len(nums) - 1)
    else:
        print(left + 1, right + 1)