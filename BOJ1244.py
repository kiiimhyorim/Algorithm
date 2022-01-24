import sys
import math
input = sys.stdin.readline

n = int(input()) #스위치 수
state = list(map(int, input().split()))
student = int(input()) #학생 수, 남학생 1, 여학생 2

for _ in range(student):
    sex, idx = map(int, input().split())
    
    if sex ==1: #남학생
        for i in range(idx-1,n,idx):#받은 인덱스부터,끝까지,idx간격으로
            if state[i] == 0:#스위치 켜져있으면 끄고, 꺼져있으면 켠다.
                state[i] =1
            else:
                state[i] = 0
                
    if sex==2: #여학생
        start, end = 0,0
        for i in range(n//2+1):
            left = (idx-1) -i #좌로 이동
            right = (idx-1) + i #우로 이동
            
            if 0<=left<n and 0<=right<n: #범위 확인
                if state[left] == state[right]: #양쪽 같은 경우
                    start, end = left, right
                    if start ==0 or end == n-1:#인덱스 마지막 도달
                        break
                else:#양쪽 다른 경우
                    if start ==0 and end ==0:#시작과 동시에 양쪽 다름
                        start =end = idx-1
                        break
                    break #다르면 바로 멈춤                  
        for i in range(start,end+1):#시작점 끝점 찾아서 스위치 상태 바꿔주기
            if state[i] ==0:
                state[i]=1
            else:
                state[i] = 0              
##출력 한줄에 20개씩##
if n <= 20:
    for i in range(n):
        print(state[i], end = ' ') 
else:
    for k in range(math.ceil(n/20)):
        for i in range(20):
            print(state[i+(20*k)], end = ' ')
            if i +(20*k) == n-1:
                break
        print()