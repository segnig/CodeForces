for _ in range(int(input())):
    s=  list(input())
    
    lis=list(map(int,s))
    n = len(lis)
    for i in range(n):
        cur=min(i+9,n-1)
        
        for j in range(cur,i,-1):
            if(lis[j]-1>lis[j-1]):
                lis[j],lis[j-1]=lis[j-1],lis[j]-1
    lis = list(map(str,lis))
    print("".join(lis))
                
            
           