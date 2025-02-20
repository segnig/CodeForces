from collections import defaultdict, Counter
for _ in range(int(input())):
    word = input()
    counter = Counter(word)
    store = defaultdict(list)
    
    for key, count  in counter.items():
        store[count].append(key)
        
    result = "".join(store[2]) * 2 + "".join(store[1])
    
    print(result)
    