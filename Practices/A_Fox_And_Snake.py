row, col = map(int, input().split())

matrix = []

for i in range(row):
    if i % 2 == 0:
        matrix.append("#" * col)
    else:
        if (i // 2) % 2== 0:
            matrix.append("." * (col - 1) + "#")
        else:
            matrix.append("#" + "." * (col - 1))
            
for row in matrix:
    print(row)