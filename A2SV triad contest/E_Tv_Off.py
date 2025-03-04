n = int(input())
segments = []
coord_set = set()

for _ in range(n):
    l, r = map(int , input().split())
    segments.append((l, r + 1))
    coord_set.add(l)
    coord_set.add(r + 1)


coord_list = sorted(coord_set)
coord_map = {v: i for i, v in enumerate(coord_list)}
m = len(coord_list)

coverage = [0] * (m + 1)
for l, r in segments:
    coverage[coord_map[l]] += 1
    coverage[coord_map[r]] -= 1

for i in range(1, m):
    coverage[i] += coverage[i - 1]

pref = [0] * m
for i in range(1, m):
    pref[i] = pref[i - 1] + (1 if coverage[i - 1] == 1 else 0)


for i, (l, r) in enumerate(segments):
    if pref[coord_map[r]] - pref[coord_map[l]] == 0:
        print(i + 1)
        break
else:
    print(-1)