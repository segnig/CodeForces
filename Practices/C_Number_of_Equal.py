input()

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

result = 0

left, right = 0, 0

for num in num2:
   
    while left < len(num1) and num1[left] < num:
        left += 1 
    while right < len(num1) and num1[right] <= num:
        right += 1 
 
    result += right - left
    
print(result)

# left1, right1 = 0, 0
# left2, right2 = 0, 0

# while right1 < len(num1) and right2 < len(num2):
#     if num1[left1] == num2[left2]:
#         while right1 < len(num1) and num1[right1] == num1[left1]:
#             right1 += 1
#         while right2 < len(num2) and num2[right2] == num2[left2]:
#             right2 += 1
#         result += (right1 - left1) * (right2 - left2)
#         left1 = right1
#         left2 = right2
        
#     elif num2[right2] < num1[right1]:
#         right2 += 1
#         left2 = right2
#     else:
#         right1 += 1
#         left2 = right2
        
# print(result)
        
    