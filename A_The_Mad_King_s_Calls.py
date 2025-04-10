for _ in  range(int(input())):
    n = input()
    result = 0
    r = "1"
    while r < n[0]:
        result += 10
        r = str(int(r) + 1)
    for i in range(len(n)):
        result += i + 1
    print(result)