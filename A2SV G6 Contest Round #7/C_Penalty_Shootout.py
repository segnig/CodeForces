def generator(nums):
    result = [[]]
    
    for n in nums:
        if n == "?":
            for res in result:
                res.append(1)
            temp = []
            for res in result:
                cop = res.copy()
                cop.pop()
                cop.append(0)
                temp.append(cop)
            result.extend(temp)
        else:
            for res in result:
                res.append(int(n))
                
    return result
            


for _ in range(int(input())):
    penality = input()
    first_players = [penality[i] for i in range(10) if i % 2 == 0]
    second_players = [penality[i] for i in range(10) if i % 2 == 1]
    
    result1 = generator(first_players)
    result2 = generator(second_players)
    
    res = 10
    
    for kick1 in result1:
        for kick2 in result2:
            g1, g2 = 0, 0
            for i in range(5):
                g1 += kick1[i]
                
                if g2 - g1 > 4 - i:
                    res = min(res, i + i + 1)
                elif g1 - g2 - 1 > 4 -i:
                    res = min(res, i + i + 1)
                    
                g2 += kick2[i]
                if abs(g1 - g2) > 4 - i:
                    res = min(res, i + i + 2)
                         
    print(res)