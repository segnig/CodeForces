def num(n, result):
    # base case
    if n == 1:
        result.append(1)
        return result
    # add the num to a result
    result.append(n)
    return num(n-1, result)

result = num(1, [])
print(result)
