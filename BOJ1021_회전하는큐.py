from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
idx_list = list(map(int, input().split()))
queue = deque(list(i for i in range(1,n+1)))
cnt = 0
for idx in idx_list:
    # 현재 원소 기준으로 왼쪽 오른쪽 길이 파악
    left = queue.index(idx)
    right = len(queue) - (left+1)
    
    if left ==0:
        queue.popleft()
        
    elif left <=right: # 왼쪽으로 이동하는게 유리할때
        queue.rotate(-left)
        queue.popleft()
        cnt+=left
    else:
        queue.rotate(right+1)
        queue.popleft()
        cnt+=right+1
        
print(cnt)