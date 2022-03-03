import sys
input = sys.stdin.readline
n = int(input())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))
    
info.sort(key = lambda x : (x[1], x[0])) #끝나는시간, 시작시간 순서로 정렬

cnt = 1
end = info[0][1]

for i in range(1,n):
    if info[i][0]>=end: #시작시간이 끝나는 시간보다 클 때
        cnt +=1
        end = info[i][1]
        
print(cnt)