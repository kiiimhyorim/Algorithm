from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

dist = [-1]*(100001)

def bfs(x):
    queue = deque()
    queue.append(x)
    dist[x] = 0
    while queue:
        x = queue.popleft()
        if x == k:
            return dist[k]
        for nx in [x+1,x-1, 2*x]:
            if 0<=nx<len(dist):
                if dist[nx] ==-1:
                    if nx !=2*x:
                        dist[nx] = dist[x]+1
                        queue.append(nx)
                    else: #이동 시간이 0 (즉 가중치 0)
                        dist[nx] = dist[x]
                        queue.appendleft(nx) #큐의 맨 앞에 삽입
                                    
if k<=n:
    print(n-k)
else:
    print(bfs(n))