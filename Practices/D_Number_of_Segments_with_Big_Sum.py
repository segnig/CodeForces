n, total = map(int, input().split())
nums = list(map(int, input().split()))
res = 0
window = 0
left = 0

for right in range(n):
    window += nums[right]
    while left <= right and  window >= total:
        res += n - right
        window -= nums[left]
        left += 1

while window >= total and left < n:
    res += 1
    window -= nums[left]
    left += 1
    
print(res)