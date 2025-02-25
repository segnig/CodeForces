n, m = map(int, input().split())

minutes = [0]
for _ in range(n):
    a, b = map(int, input().split())
    
    minutes.append(minutes[-1] + (a * b))
likes = list(map(int, input().split()))

left = 1

for minu in likes:
    while minu > minutes[left]:
        left += 1
    print(left)
    
    
from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i + 1][j + 1] = (
                    self.matrix[i + 1][j] + self.matrix[i][j + 1] +
                    matrix[i][j] - self.matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.matrix[row2 + 1][col2 + 1] - self.matrix[row2 + 1][col1] -
            self.matrix[row1][col2 + 1] + self.matrix[row1][col1]
        )

# Usage Example:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1, col1, row2, col2)