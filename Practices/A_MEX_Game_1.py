from collections import Counter

for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    result = 0
    counter = Counter(nums)
    counter = [k for k in counter.items()]
    
    counter.sort()
    
    for count in range(len(counter)):
        if count > result:
            break
        if count < counter[count][1]:
            result = counter[count][0]
            break
        else:
            result += 1
            
    print(result)
        
    
    