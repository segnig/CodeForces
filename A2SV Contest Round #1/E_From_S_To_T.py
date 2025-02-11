from collections import defaultdict

for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    
    counter_p = defaultdict(int)
    
    for char in p:
        counter_p[char] += 1
    """_summary_
    aaaaa
    
    {
        "a": 
    }
    
    """
    
    fast_index = 0
    possible = True
    
    for char in t:
        if fast_index < len(s) and s[fast_index] == char:
            fast_index += 1
        else:
            if counter_p[char] == 0:
                possible = False
                break
            else:
                counter_p[char] -= 1
    
    if possible:
        print("YES")
    else:
        print("NO")
