import sys
sys.setrecursionlimit(10**9)

#입력
m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

def dfs(x,y,color):
    global cnt
    #범위 파악
    if x>=n or x<0 or y>=m or y<0:
        return False
    
    if graph[x][y] == color and visited[x][y] == False: #아직 방문 안했고, 원하는 색이라면
        cnt+=1
        visited[x][y] = True
        dfs(x,y+1,color)
        dfs(x,y-1,color)
        dfs(x+1,y,color)
        dfs(x-1,y,color)
        return True
    return False
cnt = 0
result = [0,0]
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if dfs(i,j,'W')==True:
            result[0] += cnt**2
            cnt = 0
            
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if dfs(i,j,'B')==True:
            result[1] += cnt**2
            cnt = 0
for r in result:
    print(r, end = ' ')