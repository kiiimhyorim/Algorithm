from collections import deque
from itertools import combinations
import sys
import copy

# 입력
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 바이러스 좌표 담기
#처음부터 바이러스만 있는경우
is_full = True
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i, j])
        if graph[i][j] == 0:
            is_full = False

# m개 활성화될 바이러스 고르는 경우의 수
virus_list = list(combinations(virus, m))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    max_dist = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if copy_graph[nx][ny] != 1 and dist[nx][ny]==-1:
                    dist[nx][ny] = dist[x][y] + 1 #거리 증가
                    # 빈칸인 경우 현재 거리를 저장
                    # 이 부분을 고려안해서 몇시간 고생함 ㅜ
                    if copy_graph[nx][ny]==0:
                        max_dist = max(max_dist, dist[nx][ny])
                    queue.append([nx, ny])
                    copy_graph[nx][ny] = 2 #바이러스 전파

    # 모든 영역에 바이러스가 다 퍼졌는지 체크
    flag = True
    for i in range(n):
        if 0 in copy_graph[i]:
            flag = False
    if flag==True:
        result.append(max_dist)

result = []
for v in virus_list:
    # 활성 바이러스 큐에 담기
    copy_graph = copy.deepcopy(graph)
    queue = deque()
    dist = [[-1] * n for _ in range(n)]  # 최소거리(시간) 담을 리스트
    for a, b in v:
        queue.append([a, b])
        dist[a][b] =0

    bfs()

if result:
    if is_full: #처음부터 벽을 제외한 공간에 바이러스가 전파된 경우
        print(0)
    else:
        print(min(result))
else:# 모든 공간에 바이러스 전파에 실패한 경우
    print(-1)