from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        pop = queue.popleft()
        for i in graph[pop]:
            if visited[i] ==0: #방문 안했으면
                visited[i] = -visited[pop]
                queue.append(i)
            else:
                if visited[i] == visited[pop]:
                    return False
    return True


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    visited = [0] * (v + 1)
    flag = True  # 이분 그래프 확인해주는 변수
    # 그래프 입력 받음
    # 이때 V*V 2차원 리스트 이용하면 v*v = 최대 4억이므로 메모리 초과 발생
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for x in range(1, v + 1):
        if visited[x] ==0:
            if bfs(x) == False:
                flag = False
                break
    if flag:
        print('YES')
    else:
        print('NO')