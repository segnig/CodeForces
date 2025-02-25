def solver(arr):
    n = len(arr)
    prefix_sum = [0]
    for i in range(n):
        tn = -1 if arr[i] == 0 else 1
        prefix_sum.append(prefix_sum[-1] + tn)
    return prefix_sum

def can_transform(n, a, b):
    prefix = solver(a)

    left = 0
    right = 0
    
    while right < n:
        if a[left] == b[left]:
            left += 1
            right += 1
            continue
        else:
            right += 1
            while right < n and prefix[left] != prefix[right]:
                right += 1
            
            if right < n:
                for i in range(left, right):
                    a[i] = 1 - a[i]
                
                left = right + 1
                right = left
    
    return "YES" if a == b else "NO"


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, list(input().strip())))
    b = list(map(int, list(input().strip())))

    print(can_transform(n, a, b))
