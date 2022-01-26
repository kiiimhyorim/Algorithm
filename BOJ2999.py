import sys

data = input()
n = len(data)

#r,c 찾기
r = 1
c = n
for i in range(1,n+1):
    if n%i==0:
        if r<i and i <= n//i:
            r = i
            c = n//i

arr = [[0]*c for _ in range(r)]
idx = 0
for i in range(c):
    for j in range(r):
        arr[j][i] = data[idx]
        idx+=1
        
for i in range(r):
    print(''.join(arr[i]), end = '')