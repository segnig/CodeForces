from collections import deque

def solver(nums, k):
    max_q = deque()
    min_q = deque()
    max_q.append(nums[0])
    min_q.append(nums[0])
    
    left = 0
    result = 0
    
    for right in range(1, len(nums)):
        if max_q and nums[right] < max_q[-1]:
            while max_q and  nums[right] > max_q[0]:
                max_q.pop()
            max_q.append(nums[right])
        if nums[right] < 
            
        
        
        
        while max_q and min_q and max_q[0] - min_q[0] > k:
            if max_q[0] == nums[left]:
                max_q.popleft()
            if min_q[0] == nums[left]:
                min_q.popleft()
            result += right - left 
            left += 1
        
    



n, k = map(int, input().split())

nums = list(map(int, input().split()))


