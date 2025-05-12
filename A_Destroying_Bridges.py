for _ in range(int(input())):
    n, k = map(int, input().split())
    if k >= n -1:
        n = 1
    print(n)