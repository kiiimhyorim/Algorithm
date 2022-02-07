while True:
    data = list(map(int, input().split()))
    k = data[0]
    s = data[1:]
    if k==0:#종료 조건
        break
    
    stack = []
    def dfs(start):
        #종료 조건
        if len(stack)==6:
            print(*stack)
            return
        
        for i in range(start,k):
            if s[i] not in stack:
                stack.append(s[i])
                dfs(i+1)
                stack.pop()
                
    dfs(0)
    print()