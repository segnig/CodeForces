from collections import defaultdict
def solver(nums, n):
    counter = defaultdict(int)
    remain = 1
    remain = n
    result = []
    left = 0
    for right in range(len(nums)):
        if counter[nums[right]] == 0:
            remain -= 1
        counter[nums[right]] += 1
        while remain < 0:
            counter[nums[left]] -= 1
            if counter[nums[left]] == 0:
                remain += 1
                
            left += 1
        if not result or result[1] - result[0] < right - left:
            result = [left + 1, right + 1]
    return result
    

length, n = map(int, input().split())
nums = list(map(int, input().split()))
print(*solver(nums, n))