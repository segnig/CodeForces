def solve(note, word):
    res = float("inf")
    right = len(word) - 1
    left = 0
    res = 0
    
    while left < right:
        if word[left] != word[right]:
            if word[left] == note:
                left += 1
                res += 1
            elif word[right] == note:
                right -= 1
                res += 1
            else:
                return len(word) + 1
        else:
            right -= 1
            left += 1
    return res

for _ in range(int(input())):
    input()
    word = input()
    notes = set(word)
    
    poss = []
    for note in notes:
        poss.append(solve(note, word))
        
    ans = min(poss)
    
    if ans < len(word):
        print(ans)
    else:
        print(-1) 