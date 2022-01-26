import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = [[True]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    data[x][y] = data[y][x] = False #중복 안됨
    
cnt = 0

for i in range(1,n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            if data[i][j] and data[i][k] and data[j][k]:
                cnt+=1
print(cnt)