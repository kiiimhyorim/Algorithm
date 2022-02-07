#n과 m 9번
import copy
n, m = map(int, input().split())
nums = list(map(int, input().split())) #중복 제거

#nums.sort() 마지막에 set에 넣을거라 미리 정렬 안해도됨
    
stack = []
visited = [False]*n
result = []
def dfs():
    global result, stack
    if len(stack) == m:
        s = copy.deepcopy(stack) ## 이 부분 주의
        result.append(s)
        return
    
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            stack.append(nums[i])
            dfs()
            stack.pop()
            visited[i] = False
        
dfs()
result = sorted(list(set(list(map(tuple, result))))) #셋은 순서가 없어서 정렬 망가짐

for r in result:
    print(*r)