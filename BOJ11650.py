n = int(input())
nums = []
#좌표 입력 받기
for _ in range(n):
    nums.append(list(map(int, input().split())))

# 정렬
nums = sorted(nums, key = lambda x:(x[0],x[1]))

#출력
for n in nums:
    print(n[0], n[1])