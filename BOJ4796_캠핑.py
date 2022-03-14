import sys
input = sys.stdin.readline
i = 1
while True:
    l, p, v = map(int, input().split())
    if l ==0 and p==0 and v ==0:
        break
    ans = (v//p)*l
    q = v % p
    if q < l:
        ans += q
    else:
        ans += l
    print('Case {}: {}'.format(i, ans))
    i+=1