from collections import deque
t = int(input())
#테스트 케이스만큼 반복
for _ in range(t):
    cnt = 0
    
    #문서의 갯수, 궁금한 문서 현재 몇 번째인지
    n, idx = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    max_p = max(queue)
    
    while True:

        if queue[0]<max_p: #맨 앞 문서가 중요도가 제일 높지 않을 때
            queue.append(queue.popleft()) #맨 뒤에 넣어줌
            if idx ==0: #타겟이 맨 앞에 있으면
                idx = len(queue) - 1 #맨 뒤에 넣어줌
            else:
                idx -=1 #앞으로 이동
        elif queue[0] == max_p:#맨 앞 문서가 중요도가 제일 높으면
            cnt+=1 #출력 카운트
            queue.popleft()#출력 처리
            if idx==0:
                print(cnt)
                break
            else:
                idx -=1
                max_p = max(queue) #가장 큰 중요도 업데이트