n  = int(input())

t = n

res = ""

r = 1

while len(res) < n:
    res += str(r)
    r += 1
    
print(res[n - 1])