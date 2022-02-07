# 14889 스타트와 링크
import sys
from itertools import combinations

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
members = [i for i in range(n)] #전체 인원
teams = list(set(combinations(members, n//2))) # n/2 명만큼 팀을 뽑는 모든경우의 수

ans = 200*10 #나올 수있는 가장 큰 값으로 초기화
for start in teams:
    link = list(set(members) - set(start)) #start팀과 중복되는 인원 없게 만들어줌
    start_score = 0
    link_score = 0
    
    for s in combinations(start,2):
        start_score += graph[s[0]][s[1]]
        start_score += graph[s[1]][s[0]]
        
    for l in combinations(link,2):
        link_score += graph[l[0]][l[1]]
        link_score += graph[l[1]][l[0]]
        
    ans = min(ans, abs(start_score-link_score))
    
print(ans)