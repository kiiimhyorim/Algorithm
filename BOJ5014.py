from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int, input().split())

visited = [False]*(f +1)
visited[0] = True #0층 없음
cnt = [0]*(f+1)
def bfs(x):
    queue = deque()
    queue.append(x) #현재 위치 삽입
    visited[x] = True # 시작점 방문처리
    while queue:
        x = queue.popleft()
        if x == g:#스타트링크층에 도착
            break
        for nx in [x+u, x-d]: #위, 아래 이동
            if 1<=nx<=f and visited[nx] ==False:
                visited[nx] = True #방문처리
                cnt[nx] = cnt[x]+1
                queue.append(nx) 
                
bfs(s)
if cnt[g] == 0:
    if s == g: #시작위치와 목표가 같을때
        print(0)
    else:
        print('use the stairs')
else:
    print(cnt[g])