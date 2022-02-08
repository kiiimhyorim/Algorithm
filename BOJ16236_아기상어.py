from collections import deque
import sys

## 입력
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            graph[i][j]=2 #아기상어 크기
            start = [i,j] #아기상어 시작 좌표

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(i,j):
    visited = [[False]*n for _ in range(n)]
    visited[i][j] = True
    eat = [] #먹을 수 있는 물고기 담을 배열
    dist = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append([i,j])
    
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
                if graph[nx][ny]<=graph[i][j] or graph[nx][ny]==0: #이동 할 수 있으면
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] +1 #거리 증가
                if graph[nx][ny]<graph[i][j] and graph[nx][ny] !=0: #먹을 수 있으면
                    eat.append([nx,ny,dist[nx][ny]])
                    
    if not eat:
        return -1,-1,-1
    eat.sort(key = lambda x : (x[2], x[0], x[1]))#거리가 가까운 물고기순으로 정렬
    return eat[0][0], eat[0][1], eat[0][2] # 좌표와 거리 리턴


eat_cnt = 0 #먹은 물고기 수
time = 0
while True:
    i,j = start[0], start[1]
    ex, ey, dist = bfs(i,j)
    #print('bfs 실행 결과 : i={}, j={}, ex={}, ey={}, dist={}'.format(i,j,ex,ey,dist))
    if ex==-1:
        break
    
    graph[ex][ey] = graph[i][j] # 아기상어 이동
    graph[i][j] = 0 # 물고기 먹었으니까 0으로 바꿔줌
    start = [ex,ey] # 먹은 자리부터 다시 시작
    eat_cnt+=1 #먹은 갯수 카운트
    if eat_cnt == graph[ex][ey]: #아기상어의 크기만큼 물고기 먹으면 상어크기 증가
        eat_cnt = 0
        graph[ex][ey] +=1
    time+=dist
    
print(time)