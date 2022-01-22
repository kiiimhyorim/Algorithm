data = list(input())
ans = 0
stack = []

for i in range(len(data)):
    if data[i] =='(':
        stack.append('(')
       
    else: # ')' 일때
        if data[i-1] =='(': #그 전 입력 확인
            stack.pop()
            ans +=len(stack)
            
        else:
            stack.pop()
            ans+=1
print(ans)