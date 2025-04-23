for _ in range(int(input())):
    n, m = map(int, input().split())
    
    word = input()
    target = input()
    
    word_to_nums = [ord(char) - ord("a") for char in word]
    target_to_nums = [ord(char) - ord("a") for char in target]
    
    target_sum = sum(target_to_nums)
    
    left = 0
    right = m-1
    
    cum_sum = sum(word_to_nums[:m-1])
    
    found = False
    
    while right < n:
        cum_sum += word_to_nums[right]
        if cum_sum == target_sum:
            found = True
            break
        cum_sum -= word_to_nums[left]
        left, right = left + 1, right + 1
    
    
    if found:
        print("YES")
    else:
        print("NO")
        