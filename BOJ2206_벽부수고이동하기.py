import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
    
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    queue = deque()
    queue.append([0,0,1])
    visited[0][0][1] = 1 #시작 1이동
    while queue:
        x,y,w = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][w]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m: #범위 체크
                #이동할 곳이 벽이고, w==1 (벽을 아직 안부순경우)
                if graph[nx][ny] ==1 and w ==1:
                    visited[nx][ny][0] = visited[x][y][1] +1
                    queue.append([nx,ny,0]) # 벽 부심
                # 이동할 수 있고, 아직 방문안했으면   
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] +1
                    queue.append([nx,ny,w])
                    
    return -1

print(bfs())