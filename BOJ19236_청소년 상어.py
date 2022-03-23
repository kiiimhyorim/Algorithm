import sys
import copy

## 입력 ##
## 물고기번호, 방향, 좌표(i,j) 담아줌
graph = []
for i in range(4):
    data = list(map(int, input().split()))
    temp = []
    for j in range(0,8,2):
        num, d = data[j], data[j+1]-1
        temp.append([num, d, i,j//2])
    graph.append(temp)

dx = [-1,-1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 45도 방향 전환
def rotate(dir):
    dir +=1
    if dir == 8:
        dir = 0
    return dir

#물고기 움직임
def move_fish(arr, xpos, ypos):
    for n in range(1,17): #물고기 번호 작은순 움직임
        flag = False # 해당 번호의 물고기가 존재 여부 체크
        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == n :
                    num, d, x, y = arr[i][j]
                    flag = True
                    break

        if flag: #물고기 정보 있을 때만 동작
            for i in range(8): # 이동 할 수 있을 때 까지 회전
                nx = x + dx[d]
                ny = y + dy[d]
                # 범위 안에 있고, 현재 상어의 좌표가 아닌 경우 위치 변경
                if (0<= nx < 4 and 0<=ny<4) and (nx!=xpos or ny != ypos):
                    temp_num, temp_d = arr[nx][ny][0], arr[nx][ny][1]
                    arr[x][y][0], arr[x][y][1] = temp_num, temp_d
                    arr[nx][ny][0], arr[nx][ny][1] = num, d
                    break
                d = rotate(d) # 45도 반시계 방향 회전


def dfs(sx,sy,val,arr):
    global max_val
    val += arr[sx][sy][0]
    max_val = max(val, max_val)
    arr[sx][sy][0] = 17 #상어가 먹음

    move_fish(arr, sx, sy)
    
    #상어 움직임
    sd = arr[sx][sy][1]
    for i in range(1,5):
        nx = sx + dx[sd]*i
        ny = sy + dy[sd]*i
        if 0<=nx<4 and 0<=ny<4 and arr[nx][ny][0]<17:
            dfs(nx,ny,val,copy.deepcopy(arr))


max_val = 0
dfs(0,0,0,graph)
print(max_val)