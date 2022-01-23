from collections import deque
import sys
input = sys.stdin.readline


dx = [-2, -2, -1,-1, 1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        if x == x_target and y== y_target:
            break
        for i in range(8):
            nx = x+ dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] +1
            
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    now_x, now_y = map(int, input().split())
    x_target, y_target = map(int, input().split())
    bfs(now_x, now_y) 
            
    print(graph[x_target][y_target])