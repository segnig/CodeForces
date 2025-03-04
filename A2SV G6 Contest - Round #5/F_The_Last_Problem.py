n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

prefix = [0]

for i in range(n):
    prefix.append(prefix[-1] + a[i] * b[i])
    

ans = prefix[-1]  

for i in range(1, n):
    
    # reverse odd length of sub array
    profit = a[i] * b[i]
    left = i - 1
    right = i + 1
    
    while left > -1 and right < n:
        profit += (
            a[left] * b[right] +
            a[right] * b[left]
        )
        ans = max(
            ans, 
            profit + prefix[-1] + prefix[left] - prefix[right + 1]
        )
        left -= 1
        right += 1
        
    # reverse even length of sub array
    profit = 0
    left = i - 1
    right = i
    
    while left > -1 and right < n:
        profit += (
            a[left] * b[right] +
            a[right] * b[left]
        )
        ans = max(
            ans, 
            profit + prefix[-1] + prefix[left] - prefix[right + 1]
        )
        left -= 1
        right += 1
        
print(ans)