word = input()
target = input()

res = 0

left = len(target)

for i in range(left,len(word)):
    if word[i-left:i] == target:
        res = max(res, max(i-left, len(word) - i))
        
print(res)