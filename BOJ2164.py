import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
card = deque([i for i in range(1,n+1)])#숫자 리스트 생성
    
while True:
    #카드가 한장 남았을때까지 반복
    if len(card) ==1:
        break
        
    card.popleft()#맨 윗장 버리기
    temp = card.popleft() #다음 장 뽑기
    card.append(temp) #다음장 맨 아래에 넣기
    
print(card[0])