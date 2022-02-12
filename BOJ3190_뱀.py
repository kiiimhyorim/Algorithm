from collections import deque
import sys
## 입력 ##
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
board = [[0]*n for _ in range(n)]
for _ in range(k):
    x,y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1 #사과 위치 표시
    
info = {} #방향 전환 정보 저장 딕셔너리, 키:시간, 밸류:방향
L = int(input())
for _ in range(L):
    x,c = sys.stdin.readline().split()
    info[int(x)] = c

# 이동 방향, 북,동(우),남,서 순서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

snake = deque()
snake.append([0,0]) #시작 위치 넣어줌
time = 0 #게임 시간
d = 1 #처음엔 오른쪽을 향함
nx, ny = 0, 0

def turn(direction):
    global d
    if direction == 'L': #왼쪽 회전
        d = d-1
        if d == -1: #북->서 로 회전할때
            d = 3
    else: #오른쪽 회전
        d = d +1
        if d == 4: # 서->북 회전
            d = 0
    return d

while True:
    time+=1
    nx = nx + dx[d]
    ny = ny + dy[d]
    
    #방향 전환
    if time in info.keys():
        d = turn(info[time])
        
    if 0<=nx<n and 0<=ny<n: #범위 체크
        #몸에 부딪힌 경우
        if [nx,ny] in snake:
            break
            
        #다음 위치에 사과가 있으면 길이 증가
        if board[nx][ny] == 1:
            board[nx][ny] = 0 #사과먹음
            snake.append([nx,ny])
            
        #다음 위치에 사과가 없는 경우
        elif board[nx][ny] ==0:
            snake.append([nx,ny])
            snake.popleft() #꼬리 줄여서 길이 유지
            
    else: #범위 범어난 경우
        break
    
print(time)