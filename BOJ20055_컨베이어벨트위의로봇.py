import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
belt = deque(map(int, sys.stdin.readline().split()))
         
step = 0
robot = deque([False]*(n))

while True:
        
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = False 
        
    # 2. 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 이동 할 수 있다면 이동
    #   - 로봇이 이동하기 위해 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상
    for i in range(n-2, -1,-1):
        if robot[i] and not robot[i+1] and belt[i+1]>0: # 현재 위치에 로봇이 있고
                robot[i] = False
                robot[i+1] = True
                belt[i+1] -=1 #내구도 감소
    robot[-1] = False #로봇 내림
    
    # 3. 로봇 올림
    if robot[0] == False and belt[0]>0:
        robot[0] = True
        belt[0]-=1

                  
    cnt = belt.count(0)
    step+=1
    # 4. 종료 조건
    if cnt >=k:
        print(step)
        break