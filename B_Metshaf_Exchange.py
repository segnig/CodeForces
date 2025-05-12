for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    result = []
    
    for i in range(n):
        days = 1
        
        index = i
        while nums[index] != i+1:
            index = nums[index] - 1
            
            days += 1
        result.append(days)
    print(*result)