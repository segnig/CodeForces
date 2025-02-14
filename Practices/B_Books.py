def solver(nums, total):
    res = 0
    left = 0
    ans = 0
    
    for right in range(len(nums)):
        res += nums[right]
        while total < res:
            res -= nums[left]
            left += 1
        if res > 0:
            ans = max(ans , right - left + 1) 
    return ans

n, total = map(int, input().split())
nums = list(map(int, input().split()))
print(solver(nums, total))