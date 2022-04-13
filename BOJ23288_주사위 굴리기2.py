import sys
import copy
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

# 동, 남, 서, 북 순서 -> 시계 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [i for i in range(1,7)] #초기 주사위 칸마다 숫자가 들어 있음
def rolling_dice(d):
    temp = copy.deepcopy(dice)
    if d == 0: #동쪽
        dice[0] = temp[3]
        dice[2] = temp[0]
        dice[3] = temp[5]
        dice[5] = temp[2]

    elif d == 1: #남쪽
        dice[0] = temp[1]
        dice[1] = temp[5]
        dice[4] = temp[0]
        dice[5] = temp[4]

    elif d == 2: #서쪽
        dice[0] = temp[2]
        dice[2] = temp[5]
        dice[3] = temp[0]
        dice[5] = temp[3]

    else: #북쪽
        dice[0] = temp[4]
        dice[1] = temp[0]
        dice[4] = temp[5]
        dice[5] = temp[1]

def bfs(x,y):
    global cnt
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    num = maps[x][y]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if maps[nx][ny] == num:
                    cnt+=1
                    visited[nx][ny] = True
                    queue.append([nx,ny])
    return cnt

x, y = 0, 0
d = 0
score = 0
for kk in range(k):
    cnt = 1
    visited = [[False]*m for _ in range(n)]

    nx = x + dx[d]
    ny = y + dy[d]

    if not(0<=nx<n and 0<=ny<m): #범위 이탈
        d = (d+2)%4 #반대 방향 회전 (180도)
        nx = x + dx[d]
        ny = y + dy[d]

    rolling_dice(d) #주사위 굴러감
    b = maps[nx][ny]
    c = bfs(nx, ny)
    score += (b*c)

    # 방향 재 설정
    if dice[5] > maps[nx][ny]: #주사위 아랫면 숫자가 해당 칸 보다 클때
        d = (d+1) % 4 # 시계방향 90도 회전
    elif dice[5] < maps[nx][ny]:
        d = (d-1) % 4 # 반시계 방향 90도 회전
    x, y = nx, ny #현재 위치 업데이트

print(score)
