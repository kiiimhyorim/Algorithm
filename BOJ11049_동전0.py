n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse = True) #내림차순 (큰 수부터 정렬)

cnt = 0
for i in range(len(coins)):
    if k // coins[i] >0:
        cnt += k // coins[i]
        k = k % coins[i]
        
print(cnt)