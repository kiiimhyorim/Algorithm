n = int(input())
negative = []
positive = []
for _ in range(n):
    num = int(input())
    if num >0:
        positive.append(num)
    else:
        negative.append(num)
        
# 음수 처리
ans = 0
positive.sort(reverse = True)
negative.sort()
    
if len(negative)%2 ==0: #짝수라면
    i = 0
    while True:
        if i == len(negative):
            break
        ans += negative[i]*negative[i+1]
        i +=2
else: #홀수라면
    ans +=negative.pop()
    i = 0
    while True:
        if i == len(negative):
            break
        ans += negative[i]*negative[i+1]
        i +=2

            
#양수 처리
if len(positive) % 2 ==0: #짝수라면
    i = 0
    while True:
        if i == len(positive):
            break
        ans += max(positive[i] + positive[i+1], positive[i]*positive[i+1])
        i+=2
else: #홀수라면
    ans += positive.pop()
    i = 0
    while True:
        if i == len(positive):
            break
        ans += max(positive[i] + positive[i+1], positive[i]*positive[i+1])
        i+=2
        
print(ans)