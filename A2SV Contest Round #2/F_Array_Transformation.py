from collections import defaultdict

def same_element_min_operation(arr):
    counter = defaultdict(int)
    feq_counter = defaultdict(int)
    
    for element in arr:
        counter[element] += 1
        feq_counter[counter[element]] += 1
    
    mx = 0
    for freq in feq_counter:
        mx = max(mx, freq * feq_counter[freq])

    return len(arr) - mx

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))    
    print(same_element_min_operation(arr))
    
    
            

    
            
    
            
    
    
    
    
    
    
    
    
    
    
    