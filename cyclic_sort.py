def cyclicSort(nums):
    
    for left in range(len(nums)):
        while nums[left] != left + 1:
            correct_position = nums[left] - 1
            nums[left], nums[correct_position] = nums[correct_position], nums[left]
    return nums

nums = [1, 5, 2, 4, 3]
            
print(cyclicSort(nums))