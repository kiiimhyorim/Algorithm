import sys
import copy
input = sys.stdin.readline

n, m, x, y, k = map(int , input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
orders = list(map(int, input().split()))

# 동, 서, 북, 남 순서
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0]*6 #주사위 상태 나타내는 리스트

def rolling_dice(d):

    temp = copy.deepcopy(dice)
    if d == 1: # 동쪽으로 굴렸을 때
        # 주사위 상태 변경
        dice[0] = temp[3]
        dice[2] = temp[0]
        dice[3] = temp[5]
        dice[5] = temp[2]

    elif d == 2: # 서쪽으로 굴렸을 때
        # 주사위 상태 변경
        dice[0] = temp[2]
        dice[2] = temp[5]
        dice[3] = temp[0]
        dice[5] = temp[3]

    elif d == 3: # 북쪽으로 굴렸을 때
        dice[0] = temp[4]
        dice[1] = temp[0]
        dice[4] = temp[5]
        dice[5] = temp[1]

    else: # 남쪽으로 굴렸을 때
        dice[0] = temp[1]
        dice[1] = temp[5]
        dice[4] = temp[0]
        dice[5] = temp[4]

for d in orders:
    nx = x + dx[d-1]
    ny = y + dy[d-1]

    if 0<=nx<n and 0<=ny<m: # 범위 체크
        rolling_dice(d)
        if maps[nx][ny] == 0: # 지도의 칸이 0이면 주사위 바닥면 복사
            maps[nx][ny] = dice[5] #주사위 바닥면
        else:
            dice[5] = maps[nx][ny]
            maps[nx][ny] = 0 #칸에 쓰인 숫자 0됨
        print(dice[0])  # 이동 후 주사위 윗면 출력

        x, y = nx, ny # 이동한 경우에만 현재 위치 x, y 업데이트