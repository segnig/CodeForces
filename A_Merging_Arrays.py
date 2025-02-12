input()

def solve(nums1, nums2):
    left = 0
    left2 = 0
    result = []
    while left < (len(nums1)) and left2 < (len(nums2)):
        if nums2[left2] < nums1[left]:
            result.append(nums2[left2])
            left2 += 1
        else:
            result.append(nums1[left])
            left += 1
    return result + nums1[left:] + nums2[left2:]


nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(*solve(nums1, nums2))

