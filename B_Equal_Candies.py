for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    min_value = min(arr)
    print(sum(arr) - min_value * n)