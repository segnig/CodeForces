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

pos = {}

for _ in range(INT_INPUT()):
    input()
    word = input()
    result = []
    stack_1 = []
    stack_0 = []
    Class = 0
    for char in word:
        if char == "0":
            if stack_1:
                c = stack_1.pop()
                result.append(c)
                stack_0.append(c)
            else:
                Class += 1
                result.append(Class)
                stack_0.append(Class)
        else:
            if stack_0:
                c = stack_0.pop()
                result.append(c)
                stack_1.append(c)
            else:
                Class += 1
                result.append(Class)
                stack_1.append(Class)
        
    
        
    print(max(result))
    print(*result)
            