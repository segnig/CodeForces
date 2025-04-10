from math import *


n = int(input())

nums = list(map(int, input().split()))

prod = 1

for num in nums:
    prod *= num
    
min_num = min(nums)

result = 0

for i in range(1, ceil(sqrt(min_num) - 1)):
    if prod % i == 0:
        result += 2
if prod % int(sqrt(min_num)) == 0 and int(sqrt(min_num)) != min_num:
    result += 1
if prod % min_num == 0:
    result += 1


print(result)