import sys
input = sys.stdin.readline
while True:
    nums = list(map(int, input().split()))
    if nums[0] ==0 and nums[1] == 0 and nums[2] ==0:
        break
    nums.sort(reverse = True) #큰 수부터 정렬
    
    c = nums[0]
    a = nums[1]
    b = nums[2]
    
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')