n, k = map(int, input().split())

left = 1
right = n

def solve(v):
    r = 0
    result = 0
    while v > 0:
        if v // (k ** r) == 0:
            break
        result += v // (k ** r)
        r += 1
    return result

while left <= right:
    mid = (left + right) // 2
    res = solve(mid)
    if res < n:
        left = mid + 1
    else:
        right = mid - 1
print(left)