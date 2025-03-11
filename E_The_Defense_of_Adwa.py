t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    s=input()
    
    left = 0
    res = 0
    zero = 0
   
    while left < n:
        if s[left] == "0":
            zero += 1
        else:
            zero=0
        
        if zero == m:
            res += 1
            zero = 0
            left += k  
        else:
            left += 1
    print(res)
            
            
    