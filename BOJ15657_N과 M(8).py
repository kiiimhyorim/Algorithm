#n과 m 8번
n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
stack = []

def dfs(start):
    if len(stack)==m:
        print(*stack)
        return
    
    for i in range(start,n):
        stack.append(nums[i])
        dfs(i)
        stack.pop()
        
dfs(0)