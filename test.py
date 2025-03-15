import sym


import sys
sys.setrecursionlimit(3000)
def display(n):
    if n == 1:
        return 
    display(n-1)
    print("Segni")
    

display(5)