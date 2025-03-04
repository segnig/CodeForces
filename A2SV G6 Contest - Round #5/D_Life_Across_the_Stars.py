from heapq import heappush, heappop
y = 0
k = 0

days = []

end = []

for _ in range(int(input())):
    b, d = map(int, input().split())
    days.append((b, d))
    
days.sort()

end = []

for b, d in days:
    while end and end[0] <= b:
        heappop(end)
    heappush(end, d)
    
    if k < len(end):
        k = len(end)
        y = b
    
print(y, k)