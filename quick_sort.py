def partition(nums):
    pivot = nums[0]
    writer, reader = 1, 1
    
    while reader < len(nums):
        if pivot > nums[reader]:
            nums[writer], nums[reader] = nums[reader], nums[writer]
            writer += 1
        reader += 1
    
    nums[writer-1], nums[0] = nums[0], nums[writer - 1]
    return writer - 1

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    pivot = partition(nums=nums)
    return quickSort(nums[:pivot]) + [nums[pivot]] + quickSort(nums[pivot+1:])

nums = [1, 5, 2, 8, 34, 7, 90, 11, 454, 2, 5]
sorted_nums = quickSort(nums)

print(sorted_nums)