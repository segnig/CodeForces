from math import pow

for _ in range(int(input())):
    x, y = map(int, input().split())
    
    if y % x != 0:
        print(0, 0)
    else:
        print(1, y// x)