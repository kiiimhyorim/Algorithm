from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())
graph = []
flag = True #저장 될때부터 모든 토마토가 익은 상태인지 체크
# 3차원 리스트 입력 받음
for _ in range(h):
    temp = []
    for _ in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        if 0 in a: #안익은 토마토 존재하면 체크해줌
            flag = False
        temp.append(a)
    graph.append(temp)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
dist = [[[0] * m for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]
def bfs():  # 토마토가 익어있을  때 (1일때 함수 실행)

    while queue:
        x, y, z = queue.popleft()
        visited[z][x][y] = True
        for i in range(6):  # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:  # 범위 안에 있는 경우
                # 익지않은 토마토가 있을 때
                if visited[nz][nx][ny]==False and graph[nz][nx][ny]==0:
                    dist[nz][nx][ny] = dist[z][x][y]+1
                    visited[nz][nx][ny]= True #토마토 익음
                    graph[nz][nx][ny] = 1
                    queue.append([nx, ny, nz])

if flag == True:  # 처음부터 모든 토마토 익어있었다면
    print(0)
else:
    # bfs 실행
    queue = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] ==1:
                    queue.append([i,j,k])
    bfs()

    check = True  # bfs 실행 후모든 토마토가 익은 상황
    max_day = 0
    for k in range(h):
        for i in range(n):
            if 0 in graph[k][i]:  # 익지 않은 토마토 있으면
                check = False
            max_day = max(max(dist[k][i]), max_day)

    if check == False:
        print(-1)
    else:
        print(max_day)