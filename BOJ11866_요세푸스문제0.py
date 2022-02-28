from collections import deque

n, k = map(int, input().split())
nums = [i for i in range(1,n+1)]

result = []
queue = deque(nums)
while queue:
    queue.rotate(-(k-1))
    result.append(queue.popleft())

s = '<'
for i in range(len(result)):
    if i == len(result)-1:
        s += str(result[i]) +'>'
    else:
        s += str(result[i]) + ', '
print(s)