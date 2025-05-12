from collections import deque
for test in range(int(input())):
    input() 
    n, k = [int(i) for i in input().split()]
    friends = [int(i) for i in input().split()]
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        u, v = [int(i) for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    
    queue = deque(friends)
    dist = [-1 for _ in range(n + 1)]
    for node in friends:
        dist[node] = 0
        
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            for nei in graph[node]:
                if dist[nei] == -1:
                    dist[nei] = dist[node] + 1
                    queue.append(nei)
    
                   
    mdist = [-1 for _ in range(n + 1)]
    mdist[1] = 0
    queue = deque([1])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            for nei in graph[node]:
                if mdist[nei] == -1:
                    mdist[nei] = mdist[node] + 1
                    queue.append(nei)

    
    targeted_rooms = []
    for node in range(1, n + 1):
        if len(graph[node]) == 1:
            targeted_rooms.append(node)
    
    ans = "NO"               
    for node in targeted_rooms:
        if node == 1:
            continue
            
        if mdist[node] <= dist[node]:
            ans  = "YES"
            break
    
    print(ans)