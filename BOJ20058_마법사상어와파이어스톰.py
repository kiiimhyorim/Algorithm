import sys
import copy
from collections import deque
input = sys.stdin.readline

def rotate(L, n): #격자의 크기, 맵의 크기를 파라미터로
    temp = copy.deepcopy(graph)
    x, y = 0, 0
    for k in range(2**(2*n)//2**(2*L)): #격자의 갯수만큼 반복
        for i in range(2**L):
            for j in range(2**L):
                temp[j+x][(2**L -1)-i+y] = graph[i+x][j+y]
        a = (2**n)//(2**L)
        if (k +1) % a == 0:
            x += 2**L
            y = 0
        else:
            y += 2**L
    return temp

def check_adj():
    temp = copy.deepcopy(graph)
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < 2**n and 0 <= ny < 2**n and graph[nx][ny]>0:
                    cnt += 1
            if cnt < 3 and graph[i][j] > 0:
                temp[i][j] -= 1 #인접한칸 3개 미만이면 얼음 1 감소
    return temp

def bfs(x,y):
    global cnt
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True #방문 처리
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<2**n and 0<=ny<2**n and visited[nx][ny] == False and graph[nx][ny]>0:
                queue.append([nx,ny])
                visited[nx][ny] = True
                cnt +=1
    return cnt
### 입력 ###
n, q = map(int, input().split())
graph = []
for _ in range(2**n):
    graph.append(list(map(int, input().split())))
L_list = list(map(int, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
### 파이어스톰 실행 ###
for L in L_list:
    graph = rotate(L, n)
    graph = check_adj()

### 파이어스톰 실행 후 남아 있는 얼음의 갯수 ###
total = 0
for i in range(2**n):
    total += sum(graph[i])
print(total)

### 얼음이 연결된 덩어리중 가장 큰 덩어리의 갯수 ###
max_cnt = 0
visited = [[False]*(2**n) for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if visited[i][j] == False and graph[i][j]>0:
            cnt = 1
            max_cnt = max(max_cnt, bfs(i,j))
print(max_cnt)