import sys
input = sys.stdin.readline
data = list(input().rstrip())
target = list(input().rstrip())
stack = []

for i in range(len(data)):
    stack.append(data[i])
    if stack[-1] == target[-1]:
        temp = stack[len(stack)-len(target):]
        if target == temp:
            for _ in range(len(target)):
                stack.pop()   
            
if len(stack)==0:
    print('FRULA')
else:
    print(''.join(stack))