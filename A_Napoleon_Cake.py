n=int(input())
for i in range(n):
    t=int(input())
    arr=list(map(int,input().split()))
    stack=[]
    ans=[0]*t
    maxi=arr[-1]
    for j in range(t-1,-1,-1):
       maxi=max(maxi,arr[j])
       if maxi:
           ans[j]=1
           maxi-=1
        
    print(*ans)

        
        
        
        