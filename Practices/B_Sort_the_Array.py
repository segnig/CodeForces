n = int(input())

nums = list(map(int, input().split()))

num1 = nums.copy()

nums.sort()
left = 0
right = 0
get = False

while right < n:
    if num1[right] != nums[left]:
        while right < n and num1[right] != nums[left]:
             right += 1
        
        num1 = num1[:left] + num1[left:right+1][::-1] + num1[right +1:]
        
        
        if nums == num1:
            print("yes")
            print(left + 1, right + 1)
            get = True
            break
        else:
            print("no")
            get = True
            break
    left, right = left + 1, right + 1

if not get:
    print("yes")
    print(1, 1)
    
    
           