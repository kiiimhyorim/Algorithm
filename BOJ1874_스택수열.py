import sys
input = sys.stdin.readline

n = int(input())
answer = [] #정답
for _ in range(n):
    answer.append(int(input()))
    
temp = [] #1-n까지 넣을 스택
result = [] #결과 담을 스택
ans = [] #push, pop 기록할 스택
idx = 0 #인덱스 기록

for i in range(1,n+1):
    temp.append(i)
    ans.append('+')
    if i == answer[idx] and temp:
        idx+=1    
        result.append(temp.pop())
        ans.append('-')
        
    ## 이 부분 주의,,(틀렸던 부분)
    while temp:
        if temp[-1] == answer[idx]:
            result.append(temp.pop())
            ans.append('-')
            idx+=1
        else:
            break
         
        
while temp:
    result.append(temp.pop())
    ans.append('-')
    
if result == answer:
    for a in ans:
        print(a)
else:
    print('NO')