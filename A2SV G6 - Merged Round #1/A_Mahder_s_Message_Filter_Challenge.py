for _ in range(int(input())):
    n = int(input())
    word = input()
    
    count = 0
    for char in reversed(word):
        if char == ")":
            count += 1
        else:
            break
    
    if n - count < count:
        print("Yes")
    else:
        print("No")
        