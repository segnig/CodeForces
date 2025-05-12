from collections import defaultdict
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n , m , k = list(map(int , input().split()))
    graph = defaultdict(list)

    for _ in range(m):
        u , v = map(int , input().split())
        graph[u].append(v)
        graph[v].append(u)


    vis = set()
    stack = []
    def dfs(node , parent):
        vis.add(node)
        stack.append(node)
        for nb in graph[node]:
            if nb not in vis:
                dfs(nb , node) 
            elif nb == parent:
                continue
            else:
                if nb in stack:
                    ind = stack.index(nb)
                    cycle = stack[ind:]
                    if len(cycle) > k:
                        print(len(cycle))
                        print(*cycle)
                        return
            if stack:
                stack.pop()


    dfs(1 , -1)

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()