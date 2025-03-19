import sys, threading

def input():
    return sys.stdin.readline().strip()

def INT_INPUT():
    return int(input())

def TUPLE_INPUT():
    return input().split()

def TUPLE_INT_INPUT():
    return map(int, input().split())

def LIST_INT_INPUT():
    return list(map(int, input().split()))

def LIST_INPUT():
    return list(input().split())

t = INT_INPUT()

for _ in range(t):
    n = INT_INPUT()
    broad = []
    for l in range(n):
        row = list(input())
        count = 0
        for r in range(len(row)):
            if row[r] == "X":
                count += 1
            else:
                count = 0
            if count == 3:
                row[r] = "O"
                count = 0    
        broad.append(row[::])
    
    for i in range(n):
        count = 0  
        for j in range(n):
            if broad[j][i] == "X":
                count += 1
            else:
                count = 0
            if count == 3:
                broad[j][i] = "O"
                count = 0 
    
    print()
    for row in broad:
        print("".join(row))