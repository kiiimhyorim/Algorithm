from collections import deque
n = int(input())
maze = list(map(int, input().split()))

visited = [-1]*n
visited[0] = 0
def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for step in range(1,maze[x]+1):
            nx = x + step 
            if 0<=nx<n and visited[nx] == -1:
                visited[nx] = visited[x]+1
                queue.append(nx)
                
bfs(0)
if visited[-1] == -1:
    print(-1)
else:
    print(visited[-1])