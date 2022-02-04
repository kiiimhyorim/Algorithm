import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
    
house = [] #집 좌표 담을 리스트
chicken = [] #치킨 집 좌표 담을 리스트

#집, 치킨집 좌표를 담아줌
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1: #집이면
            house.append([i,j])
        elif maps[i][j] == 2: #치킨집이면
            chicken.append([i,j])
            
#치킨 집 m개를 골랐을 조합
chicken_list = list(combinations(chicken,m))
# m개의 치킨집을 골랐을 때 그 조합의 집과의 최소 거리 담을 리스트
result = [0]*len(chicken_list)

for h in house:#각 집의 좌표마다
    for i in range(len(chicken_list)): #치킨집 조합에서
        dis = 101
        for ch in chicken_list[i]:#가장 짧은 거리를 찾아서 result[i]에 더해줌
            temp = abs(h[0]- ch[0]) + abs(h[1]- ch[1]) #거리 계산
            dis = min(dis, temp)
        result[i] += dis
        
print(min(result))