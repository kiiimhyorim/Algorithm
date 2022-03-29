import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = []
#물고기 번호, 방향, 이동체크할 빈 리스트 담아줌
for i in range(n):
    temp = list(map(int, input().split()))
    g = []
    for j in range(n):
        g.append([temp[j],0,[]])
    graph.append(g)

#현재 방향 담아줌
dir = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        for num in range(1,m+1):
            if graph[i][j][0] == num:
                graph[i][j][1] = dir[num-1] - 1

# 방향 우선순위 리스트
d_list = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        d_list[i].append(list(map(int, input().split())))

#향기 뿌려줌
smell = [[[0,0]for _ in range(n)] for _ in range(n)]

#위, 아래, 왼, 오 순서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread_smell():
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] > 0:
                smell[i][j][0] = graph[i][j][0]
                smell[i][j][1] = k

def check_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][0]>0:
                smell[i][j][1] -= 1 #시간 감소
                if smell[i][j][1] ==0:
                    smell[i][j][0] = 0 #시간 지난 후 향기 소멸

def move():
    #동시 이동
    global shark_cnt
    for i in range(n):
        for j in range(n):
            for num in range(1, m+1):
                if graph[i][j][0] == num:
                    found = False #인접한 곳에 향기 없는 칸 확인
                    d = graph[i][j][1]
                    d_temp = d_list[num - 1][d]
                    for dd in d_temp:
                        nx = i + dx[dd - 1]
                        ny = j + dy[dd - 1]
                        if 0<=nx<n and 0<=ny<n and smell[nx][ny][0] == 0:
                            graph[nx][ny][2].append([graph[i][j][0], dd-1])
                            graph[i][j][0] = 0
                            graph[i][j][1] = 0
                            found = True
                            break
                    if not found: #인접한 곳에 향기 없는 칸이 없을 때
                        d = graph[i][j][1]
                        d_temp = d_list[num-1][d]
                        for dd in d_temp:
                            nx = i + dx[dd-1]
                            ny = j + dy[dd-1]
                            if 0<=nx<n and 0<=ny<n and smell[nx][ny][0] == num:
                                graph[nx][ny][2].append([graph[i][j][0], dd-1])
                                graph[i][j][0] = 0
                                graph[i][j][1] = 0
                                break

    #충돌 체크
    for i in range(n):
        for j in range(n):
            if len(graph[i][j][2])>1:
                nums = []
                for idx in range(len(graph[i][j][2])):
                    nums.append([graph[i][j][2][idx][0],graph[i][j][2][idx][1]])
                nums.sort(key = lambda x :x[0])

                num, d = nums[0]
                graph[i][j][0] = num
                graph[i][j][1] = d
                shark_cnt = shark_cnt - len(graph[i][j][2]) +1
                graph[i][j][2] = []
            elif len(graph[i][j][2]) ==1:
                graph[i][j][0] = graph[i][j][2][0][0]
                graph[i][j][1] = graph[i][j][2][0][1]
                graph[i][j][2] = []

shark_cnt = m
time = 0
spread_smell()
while True:
    time +=1
    if time >1000:
        print(-1)
        break
    move()
    check_smell()
    spread_smell()

    if shark_cnt ==1:
        print(time)
        break