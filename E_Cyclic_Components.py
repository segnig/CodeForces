import sys
from collections import defaultdict, deque

input = sys.stdin.readline
output = sys.stdout.write

INT_INPUT = lambda: int(input().strip())
LIST_INPUT = lambda: list(map(int, input().split()))

def isCycle(nodes, degree):
    for node in nodes:
        if degree[node] != 2:
            return False
    return True

def bfs(node, graph, components, component_id, visited):
    queue = deque([node])
    while queue:
        current = queue.popleft()
        components[component_id].append(current)
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def solve():
    n, m = LIST_INPUT()
    graph = defaultdict(list)
    degree = [0] * n
    visited = [False] * n

    for _ in range(m):
        u, v = LIST_INPUT()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    components = defaultdict(list)
    component_id = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bfs(i, graph, components, component_id, visited)
            component_id += 1
    
    count = sum(isCycle(nodes, degree) for nodes in components.values())
    output(f"{count}")

def main():
    solve()

if __name__ == '__main__':
    main()
