import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    from collections import defaultdict


    graph = defaultdict(list)

    n = int(input())

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
        



    def dfs(node, dist, parent):
        distances[node] = max(distances[node], dist)
        for nb in graph[node]:
            if nb != parent:
                dfs(nb, dist+1, node)
                
    distances = [0] * n      
    dfs(0, 0, -1)

    first = distances.index(max(distances))

    distances = [0] * n
    dfs(first, 0, -1)

    second = distances.index(max(distances))
    dfs(second, 0, -1)

    distances.sort()

    from bisect import bisect_left

    result = []

    for k in range(1, n+1):
        num_com = bisect_left(distances, k)
        
        result.append(min(num_com + 1, n))
        
    print(*result)
        
      
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
