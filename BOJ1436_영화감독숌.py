n = int(input())
cnt = 0
val = 666
while True:
    if '666'in str(val):
        cnt+=1
    if cnt==n:
        print(val)
        break
    val+=1