import sys
input = sys.stdin.readline
n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = 0
min_cost = cost[0] #처음 가격
for i in range(n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    ans += min_cost * road[i]
    
print(ans)