import sys
sys.setrecursionlimit(10**9)

#입력
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[False]*m for _ in range(n)]
is_move = ['.', 'o', 'v']
def dfs(x,y):
    global wolf
    global sheep
    #영역 파악
    if x>=n or x<0 or y>=m or y<0:
        return False

    if visited[x][y] == False and graph[x][y] in is_move:#아직 방문 안했고 이동가능
        visited[x][y] = True#방문처리
        if graph[x][y] == 'o':#양이라면
            sheep+=1
        elif graph[x][y] =='v':#늑대라면
            wolf +=1
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    return False

wolf =0
sheep = 0
result = [0,0] #양, 늑대
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            if sheep > wolf:
                wolf = 0
                result[0] += sheep
                result[1] += wolf
            else:
                sheep = 0
                result[0] += sheep
                result[1] += wolf
                
            sheep = 0
            wolf = 0
            
for r in result:
    print(r, end = ' ')
    