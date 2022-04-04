import sys
import copy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    global cnt
    global rainbow
    global normal
    queue = deque()
    queue.append([x,y])
    color = graph[x][y]
    #일반 블럭
    pos = [[x,y]]
    normal +=1

    rainbow_pos = []
    block = [[x,y]]
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
                # 무지개 블록 또는 색이 같은 일반 블록일때
                if graph[nx][ny] ==0 or graph[nx][ny]==color :
                    cnt +=1
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    block.append([nx, ny])
                    #일반 블록일 때 좌표 추가
                    if graph[nx][ny] != 0:
                        normal+=1
                        pos.append([nx,ny])
                    else:
                        rainbow +=1
                        rainbow_pos.append([nx,ny])
    #무지개 블록 재사용 가능 -> bfs 실행 완료하면 방문 풀어줌
    for rain in rainbow_pos:
        x, y = rain
        visited[x][y] = False

    pos.sort(key = lambda x:(x[0], x[1])) # 일반블록 중 행, 열이 작은 순서로 정렬
    return cnt, rainbow, normal, pos[0][0], pos[0][1], block

def gravity():
    for col in range(n):
        for row in range(n-1, -1, -1):
            if graph[row][col] == -2: #빈칸이라면
                for k in range(1, n):
                    nrow = row -k
                    if 0<=nrow<n:
                        if graph[nrow][col] ==-1:
                            break
                        elif graph[nrow][col] > -1:
                            graph[row][col] = graph[nrow][col]
                            graph[nrow][col] = -2
                            break

def rotate():
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            graph[n-1-j][i] = new_graph[i][j]

result = 0
while True:
    check = [] #모든 블록 그룹의 정보를 담음
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cnt = 1
            rainbow = 0
            normal = 0
            if graph[i][j] >0 and not visited[i][j]: #일반 블록일때만 bfs 실행
                cnt, rainbow, normal, tx, ty, temp_pos = bfs(i,j)
                temp = [cnt, rainbow, tx, ty, normal, temp_pos]
                check.append(temp)

    check.sort(key = lambda x:(x[0], x[1], x[2], x[3]), reverse=True)
    if not check:
        break
    max_val, max_normal = check[0][0], check[0][4]
    if max_val < 2 or max_normal < 1: # 블록그룹 크기 2이상, 일반블록 1개 이상 있어야함
        break
    result += max_val ** 2  # 그룹 블록의 크기 만큼 제곱
    # 지움
    for pos in check[0][5]:
        x, y = pos
        graph[x][y] = -2
    gravity()
    rotate()
    gravity()

print(result)