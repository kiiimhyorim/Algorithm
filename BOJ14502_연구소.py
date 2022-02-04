from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

n,m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

#빈 공간의 좌표를 담아줌
#빈 공간에 벽을 세울수 있기 때문
empty = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append([i,j])

#벽을 3개 세울수 있으므로 조합을 이용해서 3개를 뽑는 경우를 리스트에 담음
wall_list = list(combinations(empty, 3))

#bfs 함수 구현
dx = [1, -1, 0, 0]
dy = [0 ,0 ,1, -1]
def bfs(x,y): # 메인에서 2일때 bfs 호출
    queue = deque()
    queue.append([x,y])
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if lab_copy[nx][ny] ==0:
                    lab_copy[nx][ny] = 2 #바이러스 전파
                    queue.append([nx,ny])
                    
max_safe = 0
#벽을 세울 수 있는 경우의 수만큼 반복
for w in wall_list:
    
    #벽세우기
    lab_copy = copy.deepcopy(lab) #원본 유지위해 deepcopy  
    for i in range(3):
        x_pos, y_pos = w[i][0], w[i][1]
        lab_copy[x_pos][y_pos] = 1 
        
    # bfs 호출로 바이러스 전파
    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] ==2 :#연구실에 바이러스가 있을 때 전파
                bfs(i,j)
            
    #연구실에서 0을 갯수 찾기
    #최댓값을 찾아야하므로 max_safe 업데이트
    temp = 0
    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] ==0:
                temp +=1
    max_safe = max(max_safe, temp)
                
print(max_safe)