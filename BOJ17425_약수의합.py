import sys
input = sys.stdin.readline

Max = 1000000

dp = [1]*(Max + 1)
s = [0] * (Max + 1) #누적값

for i in range(2, Max + 1):
    j = 1
    while i*j <= Max:
        dp[i*j] +=i
        j += 1
        
for i in range(1, Max+1):
    s[i] = s[i-1] + dp[i]
    
t = int(input())
for _ in range(t):
    n = int(input())
    print(s[n])