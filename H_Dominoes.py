n, m = map(int, input().split())

def check(matrix, row, col):
    p = 0
    if matrix[row][col] == "#":
        return p
    if row > 0 and matrix[row - 1][col] == ".":
        p += 1
    if col > 0 and matrix[row][col - 1] == ".":
        p += 1
    return p
        


matrix = []

for _ in range(n):
    row = input()
    matrix.append(row)
    
prefix_matrix = [[0 for _ in range(m + 1)] for p in range(n + 1)]

pr = prefix_matrix.copy()

for r in range(1, n + 1):
    for c in range(1, m + 1):
        prefix_matrix[r][c] = (
            prefix_matrix[r-1][c] + 
            prefix_matrix[r][c-1] -
            prefix_matrix[r-1][c-1] + 
            prefix_matrix[r][c] + 
            check(matrix=matrix, row=r-1, col=c-1)
        )
        


for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    
    left = prefix_matrix[r2][c1-1]
    above = prefix_matrix[r1 -1][c2]
    result = prefix_matrix[r2][c2] - left - above + prefix_matrix[r1-1][c1-1]
    
    for i in range(r1 - 1, r2):
        if i >= 0 and c1 - 2 >= 0 and matrix[i][c1 - 2] == "." and matrix[i][c1 - 1] == ".":
            result -= 1

    for i in range(c1 - 1, c2): 
        if i >= 0 and r1 - 2 >= 0 and matrix[r1 - 2][i] == "." and matrix[r1 - 1][i] == ".":
            result -= 1     
    print(result)
