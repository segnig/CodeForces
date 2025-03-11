def TUPLE_INT_INPUT():
    return map(int, input().split())

def LIST_INT_INPUT():
    return list(map(int, input().split()))

n, k = TUPLE_INT_INPUT()
nums = LIST_INT_INPUT()

diff = [
    nums[i] - nums[i-1]  for i in range(1, n)
]

diff.sort()
for i in range(1, k):
    diff.pop()

print(sum(diff))