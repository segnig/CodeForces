from collections import Counter

def solve(a, b):
    count_1 = count_0 = 0
    left = 0 

    for right in range(len(a)):
        count_1 += a[right] == "1"
        count_0 += a[right] == "0"
        
        if count_0 == count_1:
            is_all_same = all(a[i] == b[i] for i in range(left, right + 1))
            is_all_diff = all(a[i] != b[i] for i in range(left, right + 1))
            if not (is_all_same or is_all_diff):
                return False
            left = right + 1 
    
    is_all_same = all(a[i] == b[i] for i in range(left, len(a)))
    is_all_diff = all(a[i] != b[i] for i in range(left, len(a)))
    if not (is_all_same or is_all_diff):
        return False
    return True
            
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = input().strip()
    b = input().strip()
    
    if solve(a, b):
        print("YES")
    else:
        print("NO")
