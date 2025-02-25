n = int(input())

nums = list(map(int, input().split()))
nums.sort()

if n % 2 == 0:
    print(nums[n//2 - 1])
else:
    print(nums[n//2])