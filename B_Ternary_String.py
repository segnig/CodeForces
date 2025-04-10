from collections import defaultdict

for _ in range(int(input())):
    word = input()
    
    result = float("inf")
    window = defaultdict(int)
    
    left = 0
    right = 0
    
    for right in range(len(word)):
        window[word[right]] += 1
        while window["1"] > 0 and window["2"] >  0 and window["3"] > 0:
            window[word[left]] -= 1
            result = min(result, right - left + 1)
            left += 1
        
    
    if result > len(word):
        print("0")
    else:
        print(result)
        