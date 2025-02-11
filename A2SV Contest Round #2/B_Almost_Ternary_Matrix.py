def update_matrix(matrix, row, col):
    
    
    s = 0
    directions = direction(len(matrix), len(matrix[0]), col, row)
    print(directions)
    for r, c in directions:
        if matrix[r][c] == 1:
            s += 1
            
    if round(s / len(directions)) == 0:
        matrix[r][c] = 1
        
    for r, c in directions:
        if matrix[r][c] == " ":
            matrix[r][c] = 0
            

def direction(row, col, c, r):
    cords = []
    if r - 1 >= 0:
        cords.append((r - 1, c))
    if r + 1 < row:
        cords.append((r + 1, c))
    if c - 1 >= 0:
        cords.append((r, c - 1))
    if c + 1 < col:
        cords.append((r, c + 1))
    
    return cords


for _ in range(int(input())):
    row, col = map(int, input().split())
    matrix = []
    for i in range(row):
        rows = [" " for _ in range(col)]
        matrix.append(rows)
        
    for i in range(row):
        for j in range(col):
            update_matrix(matrix, i, j)
            
    for row in matrix:
        print(" ".join(map(str, row)))
        
    