n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
rolling_sum = 0
res = float("inf")

for right in range(n):
    rolling_sum += nums[right]
    while rolling_sum >= s:
        res = min(res, right - left + 1)
        rolling_sum -= nums[left]
        left += 1

while left < n:
    if rolling_sum >= s:
        res = min(res, right - left + 1)
    rolling_sum -= nums[left]
    left += 1
if res == float("inf"):print(-1)
else:print(res)