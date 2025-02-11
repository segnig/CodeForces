for _ in range(int(input())):
    string = input()
    ind = len(string) // 2
    test = string[:ind] == string[ind:]
    if test:
        print("YES")
    else:
        print("NO")