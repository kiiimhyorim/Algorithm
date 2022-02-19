import sys
input = sys.stdin.readline
##입력
r, c, t = map(int, input().split())
graph = []
air_pos = [] #공기청정기 좌표
for i in range(r):
    graph.append(list(map(int, input().split())))
    for j in range(c):
        if graph[i][j] == -1:
            air_pos.append([i,j])

def spread(x,y): #미세먼지 확산
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and graph[nx][ny] != -1:
            cnt += 1
            add[nx][ny] += graph[x][y]//5 #미세먼지 확산양 저장
    remain[x][y] = graph[x][y] - (graph[x][y]//5)*cnt


def rotation(start_x, start_y, direction): #미세먼지 작동
    if direction == 1:  # 상단 이동
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
    else:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
    x, y = start_x, start_y + 1 #공기청정기 우측칸 부터 시작
    visited[x][y] = True
    i = 0
    while True:
        #공기 청정기 위치에 도달하면 종료
        if x == start_x and y == start_y:
            break
        nx = x + dx[i]
        ny = y + dy[i]
        if ny >= c or nx < 0 or nx >= r or ny < 0:  # 방향 전환
            i += 1
            nx = x + dx[i]
            ny = y + dy[i]

        move[nx][ny] = temp[x][y]
        visited[nx][ny] = True
        x, y = nx, ny

for _ in range(t): #t초 동안 동작
    remain = [[0] * c for _ in range(r)]  # 미세먼지가 확산 되고 남은 양 저장
    add = [[0] * c for _ in range(r)]  # 각 칸에 확산된 미세먼지 저장
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0: #미세먼지가 확산 가능한 경우
                spread(i,j)
            if graph[i][j] == -1:
                temp[i][j] == -1 #공기청정기 위치 파악
                
    # temp에 add와 remain 값을 합쳐줌
    # 이 때 공기청정기 위치 누락 주의
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                temp[i][j] = -1
            else:
                temp[i][j] = add[i][j] + remain[i][j]

    ### 공기청정기 작동
    upper_x, upper_y = air_pos[0][0], air_pos[0][1]
    lower_x, lower_y = air_pos[1][0], air_pos[1][1]

    move = [[0]*c for _ in range(r)]
    visited = [[False]*c for _ in range(r)] #이동 여부 체크
    #상단 이동
    rotation(upper_x, upper_y, 1) #상단
    rotation(lower_x, lower_y, 0) #하단
    
    #이동한칸과 이동하지 않은 칸 합침
    for i in range(r):
        for j in range(c):
            if visited[i][j]==False:
                move[i][j] = temp[i][j]
            if temp[i][j]==-1:
                move[i][j] = -1
    graph = move #다음 동작 위해 그래프 업데이트

result = 0
for i in range(r):
    result += sum(graph[i])

print(result+2)