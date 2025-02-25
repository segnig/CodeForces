n, m = map(int, input().split())

nums = list(map(int, input().split()))

pref = [0]
post = [0] * n

for i in range(1, n):
    res = nums[i - 1] - nums[i] if nums[i] < nums[i-1] else 0
    pref.append(pref[-1] + res)
    
for i in range(n - 2, -1, -1):
    res = nums[i] - nums[i + 1] if nums[i] < nums[i+1] else 0
    post[i] = post[i + 1] + res
    

    
for _ in range(m):
    a, b = map(int, input().split())
    if a < b:
        print(pref[b-1] - pref[a-1])
    else:
        print(post[a - 1] - post[b - 1])
    
