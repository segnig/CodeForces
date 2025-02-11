from collections import Counter, defaultdict

for _ in range(int(input())):
    n = int(input())
    word = input()
    
    counter_left = Counter(word[:1])
    counter_right = Counter(word[1:])
    
    left = len(counter_left)
    right = len(counter_right)
    
    result = left + right
    
    for car in word[1:-1]:
        counter_right[car] -= 1
        if car not in counter_left:
            counter_left[car] = 1
            left += 1
        if counter_right[car] == 0:
            del counter_right[car]
            right -= 1
        
        result = max(result, left + right)
        
    print(result)
        