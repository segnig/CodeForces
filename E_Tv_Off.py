import sys

def find_removable_segment(n, intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))  # Sort by start, then by descending end
    
    index_map = {tuple(intervals[i]): i + 1 for i in range(n)}  # Store original index (1-based)
    
    prefix_max = [-float('inf')] * n  # Max right endpoint up to index i
    suffix_min = [float('inf')] * n   # Min left endpoint from index i onward
    
    prefix_max[0] = intervals[0][1]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], intervals[i][1])
    
    suffix_min[n - 1] = intervals[n - 1][0]
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(suffix_min[i + 1], intervals[i][0])
    
    removable_index = -1
    
    for i in range(1, n - 1):
        if intervals[i][1] <= prefix_max[i - 1] or prefix_max[i - 1] >= suffix_min[i + 1] - 1:
            removable_index = index_map[tuple(intervals[i])]
            break
    
    if n > 1 and intervals[n - 1][1] <= prefix_max[n - 2]:
        removable_index = index_map[tuple(intervals[n - 1])]
    
    print(removable_index)
    

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    intervals = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    find_removable_segment(n, intervals)
