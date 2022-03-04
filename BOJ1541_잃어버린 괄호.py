data = list(input().split('-'))

ans = 0
for i in range(len(data)):
    s = data[i].split('+')
    if i ==0:
        for num in s:
            ans += int(num)
    else:
        temp = 0
        for num in s:
            temp += int(num)
        ans -= temp
        
print(ans)