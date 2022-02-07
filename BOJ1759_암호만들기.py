vowels = ['a', 'e', 'i', 'o', 'u'] #모음
L, C = map(int, input().split())
alpha = list(input().split())

alpha.sort() #사전순으로 순회하기 위해 정렬

stack = []
def dfs(start):
    if len(stack) == L:
        cnt_con = 0 #자음수 카운트
        cnt_v = 0 #모음수 카운트
        for i in range(L):
            if stack[i] in vowels:
                cnt_v+=1
            else:
                cnt_con +=1
        if cnt_v>= 1 and cnt_con >=2: #모음 1개이상, 자음 2개 이상이면 출력
            print(''.join(stack))
        return
    
    for i in range(start,C):
        if alpha[i] not in stack:
            stack.append(alpha[i])
            dfs(i+1)
            stack.pop()
            
dfs(0)