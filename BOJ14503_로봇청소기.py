n,m = map(int, input().split())
r,c,d = map(int, input().split())

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

#북, 동, 남, 서 순서로 방향 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽 방향 회전하는 함수
def turn_left():
    global d
    d = d-1   
    if d == -1:#북쪽에서 서쪽으로 회전하는 경우
        d = 3

#동작시작 시작
x,y = r,c
room[x][y] = 2 #자기 자리 청소
cnt = 1

while True:
    check = False
    for i in range(4):
    	#왼쪽 방향으로 회전
        turn_left()
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<m:
            if room[nx][ny] ==0:
                cnt+=1
                room[nx][ny] = 2 #방문처리
                x,y = nx, ny
                check = True
                break
                
    # 네 방향이 모두 이미 청소가 되어있는 경우
    if check == False:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0<=nx<n and 0<=ny<m:
        	# 벽이 아닌 경우 후진하고 다시 동작 실행
            if room[nx][ny] ==2:
                x,y = nx,ny
            # 벽인 경우 작동 중지
            elif room[nx][ny] ==1:
                print(cnt)
                break