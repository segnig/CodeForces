from math import ceil


for _ in range(int(input())):

    n, k, p = map(int, input().split())

    if k > n * p or k < - n * p:
        print(-1)
    else:
    
        print(ceil(abs(k / p)))
        