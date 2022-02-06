n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
stack = []

def dfs():
    if len(stack)==m:
        print(*stack)
        return
    
    for num in nums:
        if num not in stack:
            stack.append(num)
            dfs()
            stack.pop()
            
dfs()