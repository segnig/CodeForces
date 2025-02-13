def sign(n):
    return n < 0
def solver(nums):
    max_nums = 0
    flag = sign(nums[0])
    mx = nums[0]
    for n in nums:
        if flag != sign(n):
            max_nums += mx
            mx = n
            flag = sign(n)
        mx = max(mx, n)
    max_nums += mx
    return max_nums

for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    print(solver(nums))