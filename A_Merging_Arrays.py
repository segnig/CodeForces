def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
        
    return bucket

def bucket_sort(arr, n):
    result = [[] for _ in range(n)]
    min_num = min(arr)
    max_num = max(arr)
    size = max_num - min_num
    for num in arr:
        index = (num - min_num) // size
        result[int(index)].append(num)
    
    sorted_arr = []
    for nums in result:
        sorted_arr.extend(insertion_sort(nums))
    
    return sorted_arr



# Test cases
def test():
    # Test case 1
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    assert bucket_sort(arr, len(arr)) == [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897], "Test case 1 failed"
    
    # Test case 2
    arr = [0.5, 0.1, 0.9, 0.3, 0.7]
    assert bucket_sort(arr, len(arr)) == [0.1, 0.3, 0.5, 0.7, 0.9], "Test case 2 failed"
    
     # Test case 3
    arr = [3.9, 0.9, 1.9, 5.9, 2.9, 4.9]
    assert bucket_sort(arr, len(arr)) == [0.9, 1.9, 2.9, 3.9, 4.9, 5.9], "Test case 3 failed"
    
    print("All test cases passed!")

# Run test cases
test()
