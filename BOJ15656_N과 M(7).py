#n과 m 7번
n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
stack = []

def dfs():
    if len(stack)==m:
        print(*stack)
        return
    for i in range(n):
        stack.append(nums[i])
        dfs()
        stack.pop()