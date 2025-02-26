from collections import deque

class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.left = None
        self.right = None
        
class LinkedList:
    def __init__(self, val):
        self.head = Node(val=val, index=1)
        self.head.left = self.head
        self.head.right = self.head
        self.count = 1
        self.hash = {1:self.head}
        
    def insert(self, pos, val, index):
        left_node = self.hash[pos]
        new_node = Node(val=val, index=index)
        new_node.right = left_node.right
        new_node.left = left_node
        left_node.right = new_node
        left_node.right.left = new_node
        

for _ in range(int(input())):
    n, k = map(int, input().split())
    head = Node(val=k, index=1)
    head.left = head
    head.right = head
    
    number = 1
    
    
    
    
    
    
    