import sys

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

def good(c, char):
    if len(c) == 1:
        if char == c[0]:
            return 0
        return 1
    mid = len(c) // 2
    right = c[mid:]
    left = c[:mid]
    
    change_right = mid - right.count(char)
    change_left = mid - left.count(char)
    
    return min(
        change_right + good(left, chr(ord(char) + 1)), 
        change_left + good(right, chr(ord(char) + 1))
    )


for _ in range(INT_INPUT()):
    n = INT_INPUT()
    word = input()
    print(good(word, "a"))