# 톱니바퀴
t = []
for _ in range(4):
    t.append(list(map(int, input())))
k = int(input())

orders = []
# 톱니바퀴 번호와 회전방향 입력받음
for _ in range(k):
    num, ro = map(int, input().split())
    orders.append([num, ro])

#회전 함수
def rotation(num, directions):
    if directions == 1:  # 시계 방향
        t[num].reverse()  # 뒤집어줌
        temp = t[num].pop(0)  # 맨앞에꺼 뺌
        t[num].append(temp)  # 맨 뒤에 붙임
        t[num].reverse()  # 다시 뒤집어줌

    elif directions == -1:  # 반시계 방향
        temp = t[num].pop(0)  # 맨앞에꺼 뺌
        t[num].append(temp)  # 맨 뒤에 붙임


for order in orders:
    num, d = order[0] - 1, order[1]

    # 옆 톱니들 확인
    check = [0] * 4
    check[num] = d
    flag = False #연속적으로 회적이 일어나는지 체크해주는 변수
    if num == 0:
        if t[0][2] != t[1][6]:  # 극이 다르다면
            check[1] = -d
            flag = True

        if t[1][2] != t[2][6] and flag == True:
            check[2] = d
        else:
            flag = False

        if t[2][2] != t[3][6] and flag == True:
            check[3] = -d

    elif num == 1:
        if t[1][6] != t[0][2]:
            check[0] = -d

        if t[1][2] != t[2][6]:
            check[2] = -d
            flag = True

        if t[2][2] != t[3][6] and flag == True:
            check[3] = d

    elif num == 2:
        if t[2][2] != t[3][6]:
            check[3] = -d

        if t[2][6] != t[1][2]:
            check[1] = -d
            flag = True
        else:
            flag = False

        if t[1][6] != t[0][2] and flag == True:
            check[0] = d

    elif num == 3:
        if t[3][6] != t[2][2]:  # 극이 다르다면
            check[2] = -d
            flag = True

        if t[2][6] != t[1][2] and flag == True:
            check[1] = d
        else:
            flag = False
        if t[1][6] != t[0][2] and flag == True:
            check[0] = -d
    #회전 동작
    for i in range(4):
        if check[i]:
            rotation(i, check[i])

result = 0
cnt = 1
for i in range(4):
    if t[i][0] == 1:  # s극이면
        result+=cnt
    cnt *= 2

print(result)