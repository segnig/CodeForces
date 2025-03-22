import sys, threading
from collections import defaultdict

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

n = INT_INPUT()

tree = defaultdict(list)

for node in  range(1, n):
    tree[INT_INPUT()].append(node + 1)

tag = True
for node in tree:
    count = len(tree[node])
    for child in tree[node]:
        if child in tree:
            count -= 1
    if count < 3:
        print("No")
        tag = False
        break
if tag:
    print("Yes")