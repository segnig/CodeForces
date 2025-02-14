n, s = map(int, input().split())

nums = list(map(int, input().split()))

result = 0
window = 0

left = 0

for right in range(n):
    window += nums[right] 
    while left <= right and window > s:
        window -= nums[left]
        left += 1
    result += right - left + 1
    
print(result)