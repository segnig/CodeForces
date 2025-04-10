n = int(input())
from collections import defaultdict

word = input()

left = 0
right = 0
unique = len(set(word))
count = defaultdict(int)

result = n

while right < n:
    count[word[right]] += 1
    while len(count) == unique:
        result = min(result, right - left + 1)
        count[word[left]] -= 1
        if count[word[left]] == 0:
            del count[word[left]]
        left += 1
    right += 1
print(result)