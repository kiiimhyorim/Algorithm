from collections import deque
a, b = map(int, input().split())
dist = {} #메모리 초과 방지를 위해 딕셔너리 이용

def bfs():
    queue = deque()
    queue.append(a)
    dist[a] = 1
    while queue:
        x = queue.popleft()
        for nx in [x*2, int(str(x) + '1')]:
            if 0<=nx <=b:
                if nx not in dist: #아직 방문 안했다면
                    dist[nx] = dist[x]+1
                    queue.append(nx)
bfs()
if b in dist:
    print(dist[b])
else:
    print(-1)