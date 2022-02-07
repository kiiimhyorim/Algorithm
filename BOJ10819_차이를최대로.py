n = int(input())
nums = list(map(int, input().split()))
max_val = 0 #절댒값의 합이므로 0으로 설정

stack = []
visited = [False]*n
def dfs():
    global max_val
    if len(stack)==n:
        temp = 0
        for i in range(n-1):
            temp += abs(stack[i]-stack[i+1])
        max_val = max(max_val, temp)
        return
    
    for i in range(n):
        if visited[i] == False:
            stack.append(nums[i])
            visited[i] = True
            dfs()
            visited[i] = False
            stack.pop()
            
dfs()
print(max_val)