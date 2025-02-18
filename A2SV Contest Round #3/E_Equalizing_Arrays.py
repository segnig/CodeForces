def solver(num1, num2):
    res = 0 
    right1, right2 = 0, 0
    temp1, temp2 = 0, 0
    
    while right1 < len(num1) and right2 < len(num2):
        temp1 += num1[right1]
        temp2 += num2[right2]
        right2 += 1
        right1 += 1
        while right1 < len(num1) and right2 < len(num2) and temp1 != temp2:
            
            if temp2 > temp1:
                temp1 += num1[right1]
                right1 += 1
            elif temp2 < temp1:
                temp2 += num2[right2]
                right2 += 1
            if temp1 == temp2:
                break
        
        res += 1
        temp2 = temp1 = 0
        
        
    return res
            

n = int(input())
num1 = list(map(int, input().split()))
m = int(input())
num2 = list(map(int, input().split()))

if sum(num1) != sum(num2):
    print(-1)
else:
    print(solver(num1, num2))