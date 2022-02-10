import sys

# 입력
n, m = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

command = []  # 방향, 거리
for _ in range(m):
    command.append(list(map(int, sys.stdin.readline().split())))

cloud = [[False] * n for _ in range(n)]


# 비바라기 시전
cloud[n - 1][0] = True
cloud[n - 1][1] = True
cloud[n - 2][0] = True
cloud[n - 2][1] = True

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for com in command:
    # 구름 이동
    d, s = com[0], com[1]
    move_cloud = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if cloud[i][j]:  # 구름이 있다면
                # 명령 방향으로, 명령 거리만큼 이동
                nx = i + dx[d - 1] * s
                ny = j + dy[d - 1] * s
                # 0행, n행, 0열, n열 연결 되어있으므로 예외 처리
                if nx >= n or nx < 0:
                    nx = (n+nx) % n

                if ny >= n or ny < 0:
                    ny = (n+ny) % n

                move_cloud[nx][ny] = True  # 구름 이동
                a[nx][ny] += 1  # 각 구름에서 비가 내려서 저장된 물 1 증가

    cloud = move_cloud[:][:] #복사
    # 물복사버그 마법 시전
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == True:
                for k in [1, 3, 5, 7]:  # dx, dy에서 대각선방향
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and a[nx][ny]>0:  # 범위 안에 있으면
                        a[i][j] += 1
                        
    # 구름이 없고, 물이 2 이상이면 구름이 생기고, 물이 줄어든다
    # 이 때 원래 구름이 있던 곳은 False 처리해준다.
    for i in range(n):
        for j in range(n):
            if cloud[i][j]== False and a[i][j]>=2:
                a[i][j]-=2# 물 줄어듦
                cloud[i][j] = True #구름 생김
            elif cloud[i][j] == True:
                cloud[i][j] = False


result = 0
for i in range(n):
    for j in range(n):
        result += a[i][j]

print(result)