import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack=[]
answer = [0]*n
for i in range(n):
    while stack:
        if stack[-1][1]>tower[i]:
            answer[i] = stack[-1][0] +1
            break
        else:
            stack.pop()
            
    stack.append([i, tower[i]])
            
print(*answer)