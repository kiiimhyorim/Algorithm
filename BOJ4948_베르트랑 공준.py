import sys
input = sys.stdin.readline
Max = 123456 * 2
check = [True]* (Max + 1)
check[0] = check[1] = False # 0, 1은 소수가 아님

for i in range(1, Max + 1):
    if check[i] == True:
        for j in range(i*2, Max + 1, i):
            check[j] = False # 배수 지움
            
while True:
    n = int(input())
    if n ==0:
        break
    cnt = 0   
    for i in range(n+1, 2*n +1):
        if check[i]:
            cnt+=1
            
    print(cnt)