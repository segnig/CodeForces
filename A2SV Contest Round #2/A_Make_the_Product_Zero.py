input()

nums = list(map(int, input().split()))

nums = [abs(i) for i in nums]

print(min(nums))