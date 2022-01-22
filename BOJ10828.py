import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    order = list(input().split())
    
    if order[0] == 'push':
        stack.append(int(order[1]))
    
    elif order[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif order[0] =='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] =='empty':
        if stack:
            print(0)
        else:
            print(1)