from collections import deque
import sys
input = sys.stdin.readline

def bfs():  
    queue = deque()
    x,y = graph[0] #상근이 집 위치 담아줌
    queue.append([x, y])
    visited[0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(1,n+2):
            nx, ny = graph[i]
            dis = abs(nx-x) + abs(ny-y) #거리
            if visited[i]== False and dis<=1000:
                visited[i] = True
                queue.append([nx,ny])    
        
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [] #집, 편의점, 도착지 좌표 담음
    for _ in range(n+2):
        graph.append(list(map(int, input().split())))

    visited = [False]*(n+2)   
    bfs()
    
    if visited[-1]:
        print('happy')
    else:
        print('sad')