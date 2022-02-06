n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
stack = []

def dfs(start):
    if len(stack)==m:
        print(*stack)
        return
    
    for i in range(start, n):
        if nums[i] not in stack:
            stack.append(nums[i])
            dfs(i)
            stack.pop()