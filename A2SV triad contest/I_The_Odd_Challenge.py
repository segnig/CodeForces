for _ in range(int(input())):
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    pref = [0]
    
    for num in nums:
        pref.append(pref[-1] + num)
    for e in range(q):
        l, r, k = map(int, input().split())
        
        result = (r - l + 1) * k + pref[-1] - pref[r] - pref[l -1]
        
        if result % 2 == 1:
            print("YES")
        else:
            print("NO")