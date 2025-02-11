def generate_cord(row, col, r, c):
    
    cords = []
    
    # all eight cords
    for i in range(-1, 2):
        for j in range(-1, 2):
            if r + i >= 0 and r + i < row and c + j >= 0 and c + j < col:
                cords.append((r + i, c + j))
                
    return cords

def count_bonds(matrix, r, c):
    
    count = 0
    directions = generate_cord(row, col, r, c)
    
    for dr, dc in directions:
        if matrix[dr][dc] == '*':
            count += 1
                     
    return count

def check_valid(matrix, r, c):
    
    count = count_bonds(matrix, r, c)
    
    
    if count == 0 and matrix[r][c] == '.':
        return True
    elif count > 0 and matrix[r][c] == '.':
        return False
    elif count == int(matrix[r][c]):
        return True
    
    return False




row, col = map(int, input().split(' '))

matrix = []

for i in range(row):
    rows = list(input())
    matrix.append(rows)

poss = True
    
for i in range(row):
    for j in range(col):
        if matrix[i][j] != '*':
            if not check_valid(matrix, i, j):
                poss = False
                break

if poss:
    print('YES')
else:
    print('NO')
