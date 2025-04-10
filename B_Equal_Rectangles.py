from collections import Counter


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    arr.sort()
    
    left = 0
    right = len(arr) - 1
    
    flag = True
    res = arr[0] * arr[-1]
    
    while left < right:
        if arr[left] == arr[left + 1] and arr[right - 1 ] == arr[right]:
            if res != arr[left + 1] * arr[right]:
                flag = False
                break
        else:
            flag = False
            break
            
        left += 2
        right -= 2
        
    if flag:
        print("YES")
    else:
        print("NO")