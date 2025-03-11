
from math import ceil

        
    
t=int(input())

for i in range(t):
    n,k=map(int,input().split())
    # num=n*(k//(n-1))
    # cur = k//(n-1)
    ans=n*(k//(n-1))+(k%(n-1))
    
    if(ans%n)==0:
        ans-=1
    print(ans)
   