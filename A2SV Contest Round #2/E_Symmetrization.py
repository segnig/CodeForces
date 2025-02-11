# rotate 90 degrees

from math import ceil


def rotate(matrix):
    N = len(matrix)
    res = 0

    for i in range(N//2):
        for j in range(ceil(N/2)):
            sum_i = sum([matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1], matrix[N-j-1][i]])
            res += min(sum_i, 4 - sum_i)
            
    return res



for _ in range(int(input())):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, [n for n in input()])))
        
    print(rotate(matrix))
    