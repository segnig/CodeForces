def binary(num):
    result = ""
    while num > 0:
        result += str(num % 2)
        num //= 2
    return result

for _ in range(int(input())):
    n, x = map(int, input().split())
    result = []
    bin = binary(x)
    
    l = n
            
    print(bin)
    
    left = 0
    result = []
    while n  > 0 and left < len(bin):
        if bin[left] == "1":
            result.append(int(2 ** (l - (left + 1))))
            n -= 1
            x -= 2 ** (l - (left + 1))
        left += 1
    if n == 0:
        a = result.pop()
        result.append(int(a + x))
        print(*result)
    
        
        