def solver(nums, s):
    left, right = 0, 0
    result, sum_nums = 0, 0
    for right in range(len(nums)):
        sum_nums += nums[right]
        while sum_nums > s and left < right:
            sum_nums -= nums[left]
            left += 1
        if sum_nums <= s:
            result = max(result, right - left + 1)
        
    return result
    
n, s = map(int, input().split())
nums = list(map(int, input().split()))
print(solver(nums=nums, s=s))