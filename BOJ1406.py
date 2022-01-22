import sys
stack = list(sys.stdin.readline().strip())
temp = []
n = int(input())

for _ in range(n):
    order = sys.stdin.readline().strip()
    
    if order[0] =='L': #커서 왼쪽 이동, 맨 앞이면 무시
        if stack:
            temp.append(stack.pop())
        else:
            continue
            
    elif order[0] =='D':
        if temp:
            stack.append(temp.pop())
        else:
            continue
            
    elif order[0] == 'B':
        if stack:
            stack.pop()
            
    elif order[0] == 'P':
        stack.append(order[2])
        
print(''.join(stack+list(reversed(temp))))