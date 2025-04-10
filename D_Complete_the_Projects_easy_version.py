n,r=map(int,input().split())
pos = []
neg = []

for _ in range(n):
    a, b = map(int, input().split())
    if b >= 0:
        pos.append((a, b))
    else:
        neg.append((a, b))
        
pos.sort()
neg.sort()

flag = True
for a, b in pos:
    if r >= a:
        r += b
    else:
        flag = False
        break

# print(r, neg)
for a, b in neg:
    if r >= abs(b):
        r += b
    else:
        flag = False
        break

if flag and r > 0 :
    print("YES")
else:
    print("NO")
    