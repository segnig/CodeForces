from collections import Counter
for _ in range(int(input())):
    word = input()
    counter = Counter(word)
    
    if word[0] == word[-1]:
        print("NO")
    else:
        open = counter[word[0]]
        
        close = counter[word[-1]]
        
        p = 0
        for c in counter:
            if c not in [word[0], word[-1]]:
                p = counter[c]
                
        if p + min(close, open) == max(close, open):
            tag = False
            stack = []
            for v in word:
                if word[0] == v:
                    stack.append(v)
                elif word[-1] == v :
                    if stack:
                        stack.pop()
                    else:
                        print("NO")
                        tag = True
                        break
                else:
                    if counter[word[-1]] > counter[word[0]]:
                        stack.append(word[0])
                    else:
                        if stack:
                            stack.pop()
                        else:
                            print("NO")
                            tag = True
                            break
            if not tag and not stack:
                print("YES")
        else:
            print("NO")
    