from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
    
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    dist = [0]*(n+1)
    while queue:
        pop = queue.popleft() 
        for i in graph[pop]:
            if visited[i] == False:
                visited[i] = True
                dist[i]  += dist[pop]+1
                queue.append(i)
    return sum(dist)
        
result = [0]*(n+1)
for i in range(1,n+1):
    visited= [False]*(n+1)
    result[i] = bfs(i)

min_val = min(result[1:])
print(result.index(min_val))