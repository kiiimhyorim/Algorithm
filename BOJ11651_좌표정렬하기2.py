import sys
n = int(input())
pos = []
for _ in range(n):
    x,y = map(int, input().split())
    pos.append([x,y])
    
pos.sort(key = lambda x : (x[1], x[0])) ## 정렬

for p in pos:
    print(p[0], p[1])