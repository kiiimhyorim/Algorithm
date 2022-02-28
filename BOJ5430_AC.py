from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    orders = input().rstrip()
    n = int(input())
    arr = input().rstrip()
    reverse_cnt = 0
    #콤마, 대괄호 없애기
    arr = arr[1:-1]
    arr = arr.split(',')
    queue = deque(arr)
    # n==0 일때, 예외처리
    if n ==0:
        queue = []
        
    flag = 0
    for order in orders:
        if order == 'R':
            reverse_cnt +=1
        elif order == 'D':
            if queue:
                if reverse_cnt %2 ==0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print('error')
                flag = 1
                break
                
    if flag ==0:
        if reverse_cnt %2 ==0:
            print('['+','.join(queue) + ']')
        else:
            queue.reverse()
            print('['+','.join(queue) + ']')