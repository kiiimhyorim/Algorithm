import copy
from itertools import product
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
cctv_num = []
cctv_pos = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if graph[i][j] in [1, 2, 3, 4, 5]:
            cctv_num.append(graph[i][j])
            cctv_pos.append([i, j])

# 상,하,좌,우 순서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cctv = {1: [[0], [1], [2], [3]], 2: [[0, 1], [2, 3]], 3: [[0, 3], [0, 2], [1, 3], [1, 2]],
        4: [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]], 5: [[0, 1, 2, 3]]}

temp_cctv = []
for num in cctv_num:
    temp_cctv.append(cctv[num])

possible = list(product(*temp_cctv))  # 가능한 방향의 경우의 수 뽑음

# cctv를 입력순서로 저장했음
min_val = 64
for p in possible:
    temp = copy.deepcopy(graph)
    for i in range(len(p)):
        x, y = cctv_pos[i]
        for k in p[i]:
            nx = x
            ny = y
            while True:
                nx += dx[k]
                ny += dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break
                if temp[nx][ny] == 6:
                    break
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 7

    # 사각지대 갯수 세기
    cnt = 0
    for i in range(n):
        cnt += temp[i].count(0)

    min_val = min(cnt, min_val)

print(min_val)