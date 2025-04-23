import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, m, k = map(int, input().split())
    grid = []

    start_pos = None
    
    for i in range(n):
        row = input()
        grid.append(list(row))
        if "X" in row:
            start_pos = (i, row.index("X"))

    directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    dir_to_char = {
        (1, 0): "D",
        (0, -1): "L",
        (0, 1): "R",
        (-1, 0): "U"
    }

    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < m and grid[r][c] != '*'

    has_move = any(
        is_valid(start_pos[0] + dr, start_pos[1] + dc)
        for dr, dc in directions
    )

    if not has_move or k % 2 == 1:
        print("IMPOSSIBLE")
        return

    result = []
    r, c = start_pos

    for _ in range(k // 2):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                result.append(dir_to_char[(dr, dc)])
                r, c = nr, nc
                break

    reverse_map = {
        "D": "U",
        "U": "D",
        "L": "R",
        "R": "L"
    }

    second_half = [reverse_map[ch] for ch in reversed(result)]
    result.extend(second_half)

    print("".join(result))

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    t = threading.Thread(target=main)
    t.start()
    t.join()
