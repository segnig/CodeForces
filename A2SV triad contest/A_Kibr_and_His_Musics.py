n, m = map(int, input().split())

minutes = [0]
for _ in range(n):
    a, b = map(int, input().split())
    
    minutes.append(minutes[-1] + (a * b))
likes = list(map(int, input().split()))

left = 1

for minu in likes:
    while minu > minutes[left]:
        left += 1
    print(left)