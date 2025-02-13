from collections import Counter

def solver(nums, k, counter):
    max_diff = -1 
    last_num = nums[0]
    result = [-1, -1]
    left = 0
    for right in range(len(nums)):
        if nums[right] - last_num > 1:
            left = right
            last_num = nums[right]
            continue
        if counter[nums[right]] < k:
            if right < len(nums) -1:
                left = right + 1 
        else:
            if right - left + 1 > max_diff:
                result = [nums[left], nums[right]]
                max_diff = right - left
                
        last_num = nums[right]
    return result if result != [-1, -1] else [-1]
    

for _ in range(int(input())):
    _p, k = map(int, input().split())
    nums = list(map(int, input().split()))
    counter = Counter(nums)
    nums = [key for key in counter]

    nums.sort()
    print(*solver(nums, k, counter))