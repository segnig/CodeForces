from collections import defaultdict
n, nq = map(int, input().split())
nums = list(map(int, input().split()))

window = defaultdict(int)
have_uni = 0
left = 0
result = 0

for right in range(n):
    while have_uni == nq and window[nums[right]] == 0:
        result += right - left
        window[nums[left]] -= 1
        if window[nums[left]] == 0:
            have_uni -= 1
        left += 1
    if window[nums[right]] == 0:
        have_uni += 1
    window[nums[right]] += 1
    
for i in range(left, n):
    result += n - i
print(result)   