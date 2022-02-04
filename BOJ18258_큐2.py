from collections import deque
import sys
n = int(sys.stdin.readline())

queue = deque()
for _ in range(n):
    order = list(sys.stdin.readline().strip().split())
    
    if order[0] == 'push':
        queue.append(int(order[1]))
        
    elif order[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
            
    elif order[0] == 'size':
        print(len(queue))
        
    elif order[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
            
    elif order[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            
    elif order[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])