n, m = map(int, input().split())
nums = list(map(int, input().split()))

stack = []
result = []
nums.sort()
def dfs(start):
    if len(stack)==m:
        s = stack[:]
        result.append(s)
        return
    for i in range(start, n):
        stack.append(nums[i])
        dfs(i)
        stack.pop()
        
dfs(0)
result = sorted(list(set(list(map(tuple,result)))))
for r in result:
    print(*r)