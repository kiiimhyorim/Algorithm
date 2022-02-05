import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))
nums = []
for i in range(n):
    nums.append([temp[i], i])
    
nums.sort(key = lambda x:x[0])

result = [0]*n
cnt = 0
for i in range(n-1):
    if nums[i][0] == nums[i+1][0]:
        result[nums[i+1][1]] = cnt
    else:
        cnt+=1
        result[nums[i+1][1]] = cnt
        
print(*result)