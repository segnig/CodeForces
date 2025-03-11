n, total = map(int, input().split())

d, r = divmod(total, n)

d += 1 if r > 0 else 0

print(d)