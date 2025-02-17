k = int(input())
from collections import Counter
nums = []
string = input()
for n in string:
    nums.append(int(n))
    
pref = [0]
for n in nums:
    pref.append(pref[-1] + n)
    
counter = Counter(pref)
res = 0
if k == 0:
    list_str = string.split("1")
    for s in list_str:
        res += (len(s)) * (len(s) + 1)// 2
    
    print(res)
else:
    for n in counter:
        res += counter[n] * counter.get(n -k, 0)
    print(res)