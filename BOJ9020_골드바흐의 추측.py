import sys
input = sys.stdin.readline
Max = 10000
check = [True]* (Max + 1)
check[0] = check[1] = False # 0, 1은 소수가 아님

for i in range(1, Max + 1):
    if check[i] == True:
        for j in range(i*2, Max + 1, i):
            check[j] = False # 배수 지움
            
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n//2, 1, -1):
        if check[n-i] and check[i]:
            print(i, n-i)
            break