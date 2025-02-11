n = int(input())

index = 0
word = input()
result = ""
repeat = 1
while index < len(word):
    result += word[index]
    index += repeat
    repeat += 1
    
    
    
print(result)