input()
num = list(map(int, input().split()))

def odd(num):
    tag = num[0] % 2 == 0
    for i in num[1:]:
        if i % 2 == 1 and tag:
            return True
        if i % 2 == 0 and not tag:
            return True
    return False

if odd(num):
    num.sort()
    print(*num)
else:
    print(*num)