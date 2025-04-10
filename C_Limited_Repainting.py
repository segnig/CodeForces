def solve(nums, word, k, threshold):
    count, tag = 0, False
    for i in range(len(word)):
        if word[i] == "B" and nums[i] > threshold:
            if not tag:
                count += 1
                tag = True
        if word[i] == "R" and nums[i] > threshold:
            tag = False
    return count <= k

for _ in range(int(input())):
    n, k = map(int, input().split())
    word = input().strip()
    nums = list(map(int, input().split()))

    left, right, result = 0, max(nums), max(nums)
    
    while left <= right:
        mid = (left + right) // 2
        if solve(nums, word, k, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(result)
