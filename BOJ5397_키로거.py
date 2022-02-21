import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    data  = list(input().rstrip())
    stack = []
    temp = []
    for i in range(len(data)):
        if data[i] == '<':
            if stack:
                temp.append(stack.pop())
        elif data[i] == '>':
            if temp:
                stack.append(temp.pop())

        elif data[i] == '-':
            if stack:
                stack.pop()

        else:
            stack.append(data[i])
    result = []

    for i in range(len(stack)):
        result.append(stack[i])
    while temp:
        result.append(temp.pop())
    print(''.join(result))