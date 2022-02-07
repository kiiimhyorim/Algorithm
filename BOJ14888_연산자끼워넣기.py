from itertools import permutations
n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
operations = [] #연산자를 담는 배열

#입력받은 연산자를 n-1 만큼 확장
#0:덧셈, 1:뺄셈, 2:곱셈, 3:나눗셈
for i in range(4):
    if op[i]>1:
        for j in range(op[i]):
            operations.append(i)
    else:
        if op[i]==0:
            continue
        else:
            operations.append(i)
        
operations = list(set(permutations(operations,n-1)))#연산자의 모든경우의 수 파악

min_val = 100**11 #나올 수 있는 최댓값으로 초기화
max_val = -100**11 #나올 수 있는 최솟값으로 초기화

for operation in operations:
    temp = nums[0]#첫번째 값으로 초기화
    for i in range(n-1):
        if operation[i]==0: #덧셈
            temp+=nums[i+1]
        elif operation[i]==1:#뺄셈
            temp-=nums[i+1]
        elif operation[i] ==2:#곱셈
            temp*=nums[i+1]
        elif operation[i]==3:#나눗셈
            if temp<0:#음수인 경우
                temp = -temp #음수로 바꿈
                temp = temp//nums[i+1]
                temp = -temp#다시 음수로 바꿔줌
            else:
                temp = temp//nums[i+1]
    min_val = min(min_val, temp)
    max_val = max(max_val, temp)
    
print(max_val)
print(min_val)