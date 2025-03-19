import math
for _ in range(int(input())):
    n = int(input())
    
    result = []
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            result.append(i)
            
    get = False
    
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            temp = n // (result[i] * result[j])
            if n % (result[i] * result[j]) == 0 and n / (result[i] * result[j]) >= 2:
                if temp != result[i] and result[j] != temp:
                    print("YES")
                    print(result[i], result[j], temp)
                    get = True
                    break
        if get:
            break
    if not get:
        print("NO")
                     