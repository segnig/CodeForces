for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    ans = []
    nums = nums[::-1]
    while nums:
        if(len(nums)%2==0):
            k=nums.pop()
            if k>nums[-1]:
                ans.append(nums.pop())
            ans.append(k)
        else:
            ans.append(nums.pop())

    for i in range(1,n):
        if(ans[i]<ans[i-1]):
            print("NO")
            break
    else:
        print("YES")
            