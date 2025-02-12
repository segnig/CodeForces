import heapq


for _ in range(int(input())):
    n, l, r = map(int, input().split(','))
    nums = list(map(int, input().split()))
    
    ans1 = 0
    nums_range = nums[l - 1: r]
    nums_range = heapq.heapify(nums_range)
    
    left_range = heapq.heapify(nums[:l])
    right_range = heapq.heapify(nums[r:])
    
    while left_range and left_range[0] < nums_range[0]:
        heapq.heappop(left_range)
    
    
    
    