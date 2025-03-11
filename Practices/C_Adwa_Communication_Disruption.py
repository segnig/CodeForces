for _ in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    
    n,q = map(int,input().split())
    string = [[],s1[::],s2[::]]
    for __ in range(q):
        lis =list( map(int,input().split()))
        if(len(lis)==1):
            t1 = "".join(string[1])
            t2 = "".join(string[2])
            print(t1, t2)
            if(t1==t2):
                print("YES")
            else:
                print("NO")
        elif len(lis)==2:
            string[1][lis[1]-1], string[2][lis[1]-1] = string[2][lis[1]-1], string[1][lis[1]-1]
            # print(string)
        else:
           string[lis[1]][lis[2]-1], string[lis[3]][lis[4]-1]=string[lis[3]][lis[4]-1],string[lis[1]][lis[2]-1]
                
    
    