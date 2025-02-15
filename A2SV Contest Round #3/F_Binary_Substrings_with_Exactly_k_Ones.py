k = int(input())
from collections import Counter
nums = []
for n in input():
    nums.append(int(n))
    
pref = [0]
for n in nums:
    pref.append(pref[-1] + n)
    
counter = Counter(pref)
count = 1
nums = list(set(pref))
nums.sort()
res = 0

left = 0
right = 0
if k == 0:
    for i in range(counter[0]):
        res += i
    print(res)
else:
    while right< len(nums):
        if nums[right]  - nums[left] == k:
            res += counter[nums[left]] * counter[nums[right]]
            right += 1
            left += 1
        elif nums[right]  - nums[left] > k:
            left += 1
        else:
            right += 1
            
    print(res)
