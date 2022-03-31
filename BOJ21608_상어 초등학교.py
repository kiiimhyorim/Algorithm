import sys
input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n*n):
    students.append(list(map(int, input().split())))

arr = [[0]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def find_pos(info):
    num = info[0] #해당 학생 번호
    like = info[1:] #좋아하는 학생 번호 리스트

    #현재 교실 순회 -> 좋아하는 학생 좌표 찾음
    pos = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] in like:
                pos.append([i,j])

    #좋아하는 학생이 없다면 -> 인접한 빈칸 갯수 파악
    if len(pos) ==0:
        blank = []
        for i in range(n):
            for j in range(n):
                if arr[i][j] ==0:
                    x, y = i, j
                    cnt = 0
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==0:
                            cnt+=1
                    blank.append([cnt,0,i,j]) #인접한 빈칸의 수와 좌표를 담음
    #좋아하는 학생이 있을 때
    else:
        like_pos = []
        for i in range(n):
            for j in range(n):
                if arr[i][j] ==0:
                    x, y = i, j
                    cnt = 0
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] in like:
                            cnt+=1
                    like_pos.append([cnt,i,j])

        like_pos.sort(key = lambda x : (-x[0],x[1], x[2]))
        blank = []
        for pos in like_pos:
            cnt, x, y = pos
            blank_cnt = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<n and 0<=ny<n and arr[nx][ny]==0:
                    blank_cnt +=1
            blank.append([cnt,blank_cnt,x,y])
    blank.sort(key = lambda x:(-x[0],-x[1], x[2],x[3] )) #좋아하는 학생 인접칸, 빈 인접칸, 행, 열 작은 순서로 정렬

    return blank[0][2], blank[0][3] #좌표 리턴

for s in students:
    num = s[0] #학생 번호
    x, y = find_pos(s)
    arr[x][y] = num
#만족도
score = [0, 1, 10, 100, 1000]
ans = 0
for s in students:
    num = s[0]
    like = s[1:]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny] in like:
                        cnt +=1
                ans += score[cnt]
print(ans)