# n과 m 11번
import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
stack = []
result = []

def dfs():
    if len(stack) == m:
        s = stack[:]
        result.append(s)
        return
    for i in range(n):
        stack.append(nums[i])
        dfs()
        stack.pop()
        
dfs()

result = sorted(list(set(list(map(tuple,result)))))

for r in result:
    print(*r)