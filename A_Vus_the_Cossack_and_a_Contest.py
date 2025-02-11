n , m, k = map(int, input().split())

test = min(m, k)

if test >= n:
    print("Yes")
else:
    print("No")