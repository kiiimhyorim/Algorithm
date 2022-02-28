import sys
input = sys.stdin.readline
n ,m ,k = map(int, input().split())
fireball = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r-1, c-1, m, s, d])
    
graph = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k): #k번 명령 실행
    #파이어볼 이동
    while fireball:
        x, y, m, s, d = fireball.pop()
        # 1-N 행,열이 연결되어 있음
        nx = (x + s*dx[d]) % n
        ny = (y + s*dy[d]) % n
        graph[nx][ny].append([m, s, d])
        
    # 한 곳에 2개 이상인지 체크
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) > 1:
                sum_m, sum_s, cnt_even, cnt_odd, cnt = 0, 0, 0, 0, len(graph[i][j])
                while graph[i][j]:
                    m, s, d = graph[i][j].pop()
                    sum_m +=m
                    sum_s += s
                    if d % 2 ==0:
                        cnt_even+=1
                    else:
                        cnt_odd +=1
                        
                if cnt_odd == cnt or cnt_even == cnt:
                    dd = [0, 2, 4, 6]
                else:
                    dd = [1, 3, 5, 7]
                    
                if sum_m // 5 > 0: #0인 경우 소멸되기 때문에, 0보다 큰 경우 파이어볼이 4개로 나누어짐
                    for d in dd:
                        fireball.append([i,j,sum_m//5, sum_s//cnt, d])
                        
            if len(graph[i][j]) ==1:
                fireball.append([i,j] + graph[i][j].pop())
                
ans = 0
for f in fireball:
    ans += f[2]
    
print(ans)