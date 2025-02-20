def check(matrix, x, y):
    hori = 0
    vert = 0
    if x > 0:
        if matrix[x-1][y] == ".":
            hori = 1
    if y > 0:
        if matrix[x][y - 1] == ".":
            vert = 1     
    return hori, vert
    
r, c = map(int, input().split())

matrix = []

for _ in range(r):
    row = input()
    matrix.append(row)
    
pr = [[[0, 0] for p in range(c + 1)] for _ in range(r + 1)]


for row in range(1, r + 1):
    for col in range(1, c + 1):
        if matrix[row - 1][col - 1]:
            a, b = check(matrix=matrix, x=row - 1, y=col- 1)
        else:
            a, b = 0, 0
        pr[row][col][0] = a + pr[row][col - 1][0] + pr[row - 1][col][0] - pr[row - 1][col - 1][0]
        pr[row][col][1] = b + pr[row][col - 1][1] + pr[row - 1][col][1] - pr[row - 1][col - 1][1]

co_pr = []
for row in pr:
    rrr = []
    for cell in row:
        rrr.append(sum(cell))
    co_pr.append(rrr)
        
for row in co_pr:
    print(row)  
        
for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    
    above0 = pr[r2][c2][0] - pr[r1-1][c2][0]
    above1 = pr[r2][c2][1] - pr[r1-1][c2][1]
    
    left0 = pr[r2][c2][0] - pr[r1][c1 -1][0]
    left1 = pr[r2][c2][0] - pr[r1][c2 -1][1]
    
    two = pr[r1-1][c1-1][0] + pr[r1-1][c1-1][1]
    
    total = pr[r2][c2][0] + pr[r2][c2][1]
    
    print(total + two - (left0 + left1 + above0 + above1))
    
        
        
    
    
