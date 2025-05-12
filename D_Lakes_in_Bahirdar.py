import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, m, k = map(int, input().split())
    lakes = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    grid = []
    for _ in range(n):
        row = [col for col in input()]
        grid.append(row)
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    def inbound(row, col):
        return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
    def dfs(grid, visited, row, col):
        nonlocal canditate, is_not
        if not inbound(row=row, col=col):
            is_not =  True
            return
        if grid[row][col] == "*":
            return
        
        if visited[row][col]:
            return
        
        visited[row][col] = True
        canditate.append((row, col))
        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change
            
            dfs(grid, visited, new_row, new_col)
                    
    for i in range(n):
        for j in range(m):
            if grid [i][j] == ".":
                canditate = []
                is_not = False
                dfs(grid=grid, visited=visited, row=i, col=j)
                if not is_not:
                    lakes.append(canditate)
    
    lakes.sort(key=lambda x: len(x))
    
    m = len(lakes) - k
    count = 0
    for _ in range(m):
        for x, y in lakes[_]:
            grid[x][y] = "*"
            count += 1
    print(count)
    for row in grid:
        print(*row,sep="")
            
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
