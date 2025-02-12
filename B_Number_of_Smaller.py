n, m = map(int, input().split())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

index = 0
result = []
for num in nums2:
    while index < len(nums1) and num > nums1[index]:
        index += 1
    result.append(index)
    
print(*result)