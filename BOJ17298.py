n = int(input())
data = list(map(int, input().split()))

result = [-1]*n #결과 배열 -1로 초기화
stack = []

for i in range(n):
    while stack and stack[-1][0]<data[i]:
        temp, idx = stack.pop()
        result[idx] = data[i]
    stack.append([data[i], i])
    
print(*result)