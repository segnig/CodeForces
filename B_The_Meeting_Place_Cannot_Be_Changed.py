n = int(input())

coordinates = list(map(int, input().split()))
speeds = list(map(int, input().split()))

def solver(time):
    min_x = float("inf") 
    max_x = float("-inf")
    for c, s in zip(coordinates, speeds):
        delta = s*time
        min_x = min(c + delta, min_x)
        max_x = max(c - delta, max_x)
    return min_x >= max_x

thresholds = 10 ** (-6)

left = 0
right = max(coordinates) - min(coordinates)

while (right - left) > thresholds:
    mid = (left + right) / 2
    if solver(mid):
        right = mid
    else:
        left = mid
print(right)