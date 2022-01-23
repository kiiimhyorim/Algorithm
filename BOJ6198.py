import sys
input = sys.stdin.readline

n = int(input())
building = []
for _ in range(n):
    building.append(int(input()))
    
stack = []
cnt = 0

for i in range(n):
    while stack and stack[-1] <= building[i]:
        stack.pop()
        
    stack.append(building[i])
    cnt += len(stack)-1
    
print(cnt)