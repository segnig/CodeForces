from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    word = input()
    graph = defaultdict(list)
    
    left = False
    right = False
    
    for i in range(n):
        if word[i] == "<":
            left = True
        if word[i] == ">":
            right = True
            
    if left and right:
        count = 0
        for i in range(-1, n-1):
            if word[i] == "-" or word[i+1] == "-":
                count += 1
        print(count)
    else:
        print(n)