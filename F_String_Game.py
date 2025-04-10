t = input().strip()
p = input().strip()
nums = list(map(int, input().split()))
nums = [num - 1 for num in nums] 

def solve(mid, t, p, nums):
    removed_i = set(nums[:mid]) 
    index = 0 
    
    for i in range(len(t)):
        if i in removed_i:
            continue 
        if t[i] == p[index]:
            index += 1
            if index == len(p):
                return True
    return False

left = 0
right = len(nums)
best = 0

while left <= right:
    mid = (left + right) // 2
    if solve(mid, t, p, nums):
        best = mid 
        left = mid + 1
    else:
        right = mid - 1

print(best)