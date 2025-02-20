n, k = map(int, input().split())

nums = list(map(int, input().split()))

prefix_sum = [0]

for num in nums:
    prefix_sum.append(prefix_sum[-1] + num)
    
result = 0

for i in range(n - k + 1):
    result += prefix_sum[i + k] - prefix_sum[i]

result /=  n - k + 1   
print("%f" % result)