import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    t = int(input())

    for qq in range(t):
        n, m = map(int, input().split())

        grid = []

        for _ in range(n):
            row = list(map(int, input().split()))
            grid.append(row)

        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, visited, row, col):
            nonlocal temp
            if grid[row][col] == 0:
                return
            temp += grid[row][col]
            visited[row][col] = True
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                        dfs(grid, visited, new_row, new_col)
        
        result = 0 
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    temp = 0
                    dfs(grid=grid, visited=visited, row=i, col=j)
                    result = max(temp, result)
        print(result)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


