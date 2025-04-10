def find(x, n, m):
    count = 0
    for i in range(1, n + 1):
        count += min(x // i, m)
    return count

def solve(n, m, k):
    left, right = 1, n * m
    while left <= right:
        mid = (left + right) // 2
        if find(mid, min(n, mid), m) >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left

n, m, k = map(int, input().split())

result = solve(n, m, k)
print(result)