def solver(nums, x, n):
    nums1 = nums[:n]
    nums2 = nums[n:]
    
    for i in range(n):
        if nums2[i] - nums1[i] < x:
            return False
    return True


for _ in range(int(input())):
    n, x = map(int, input().split())
    
    nums = list(map(int, input().split()))
    
    nums.sort()
    
    test = solver(nums, x, n)
    
    if test:
        print("YES")
    else:
        print("NO")
    
    