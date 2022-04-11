import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
zero = -1
for _ in range(n):
    temp = list(map(int, input().split()))
    zero += temp.count(0)
    graph.append(temp)

graph[(n-1)//2][(n-1)//2] = -1 #상어 자리 표시

orders = []
for _ in range(m):
    orders.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0 ]
dy = [0, 0, -1, 1]

def make_one(step,mx,my):
    global num
    for _ in range(step+1):
        sx = init['sx'] + mx
        sy = init['sy'] + my
        init['sx'], init['sy'] = sx, sy
        if sx < 0 or sy < 0 or sx>=n or sy>=n:
            break
        pos.append([num, graph[sx][sy], sx,sy])
        num += 1
        
def breaking(d, s):
    global zero
    x, y = (n-1)//2, (n-1)//2
    for i in range(1, s+1):
        nx = x + dx[d-1]*i
        ny = y + dy[d-1]*i
        # 0을 중복으로 세면 안됨!!!!!!!!!!
        if graph[nx][ny] != 0:
            zero += 1
        graph[nx][ny] = 0 #빈칸 처리

    for i in range(n*n-1): #일차원 리스트 처리
        num, x, y = pos[i][0], pos[i][2], pos[i][3]
        if graph[x][y] ==0:
            pos[num][1] = 0

def move():
    while True:
        prev = pos[0][1] #구슬 번호
        px, py = pos[0][2], pos[0][3]
        for i in range(1, n*n-1):
            x,y = pos[i][2], pos[i][3]
            if prev ==0: #이전칸이 빈칸일 때
                pos[i-1][1] = pos[i][1]
                pos[i][1] = 0

                graph[px][py] = graph[x][y]
                graph[x][y] = 0
            prev = pos[i][1]
            px, py = x, y
        zero_cnt = 0
        for i in range(n*n- zero-1, len(pos)):
            if pos[i][1] ==0:
                zero_cnt +=1
        if zero_cnt == zero:
            break

def find_explosion():
    prev = pos[0][1]  # 구슬 번호
    temp = [[pos[0][0], prev, pos[0][2], pos[0][3]]]
    for i in range(1, n*n-1):
        if prev != pos[i][1]:
            if len(temp)>=4:
                del_pos.append(temp)
            temp = [[pos[i][0], pos[i][1], pos[i][2], pos[i][3]]]
            prev = pos[i][1]
            continue

        if prev == pos[i][1]:
            temp.append([pos[i][0], pos[i][1], pos[i][2], pos[i][3]])
        prev = pos[i][1]

def explosion():
    global zero
    for i in range(len(del_pos)):
        for j in range(len(del_pos[i])):
            num, ball, x,y = del_pos[i][j]
            graph[x][y] = 0
            pos[num][1] = 0
            zero +=1 # 0의 갯수 파악해줘야함

def find_group():
    prev = pos[0][1]  # 구슬 번호
    temp = [[pos[0][0], prev, pos[0][2], pos[0][3]]]
    for i in range(1, n * n - 1):
        if prev != pos[i][1]:
            groups.append(temp)
            temp = [[pos[i][0], pos[i][1], pos[i][2], pos[i][3]]]
            prev = pos[i][1]
            continue

        if prev == pos[i][1]:
            temp.append([pos[i][0], pos[i][1], pos[i][2], pos[i][3]])
        prev = pos[i][1]
def change():
    global zero
    for i in range(len(groups)):
        a, b = len(groups[i]), groups[i][0][1]
        for j in range(i*2, i*2 +2):
            if j >= len(pos):
                break
            num, ball, x, y = pos[j]
            if j%2==0:
                graph[x][y] = a
                pos[num][1] = a
            else:
                graph[x][y] = b
                pos[num][1] = b
    # 0 갯수 업데이트
    for i in range(n):
        zero += graph[i].count(0)

ans = 0
# 일차원 리스트로 변경
pos = []
num = 0
init = {'sx': (n - 1) // 2, 'sy': (n - 1) // 2}
for i in range(n):
    if i % 2 == 0:
        make_one(i, 0, -1)
        make_one(i, 1, 0)
    else:
        make_one(i, 0, 1)
        make_one(i, -1, 0)

for mm in range(m):
    d, s = orders[mm]
    breaking(d,s)
    while True:
        move()
        del_pos = []
        find_explosion()
        #점수 계산
        for d in del_pos:
            ans += (d[0][1]*len(d))
        explosion()
        if len(del_pos) ==0:
            break

    groups = []
    find_group()
    zero = 0
    change()

print(ans)