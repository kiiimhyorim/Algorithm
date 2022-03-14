import sys
input = sys.stdin.readline
n, m = map(int, input().split())
info = []
for _ in range(m):
    info.append(list(map(int, input().split()))) #패키지, 낱개 가격
    
info.sort(key = lambda x : (x[0], x[1])) #패키지가격 우선 정렬
ans_package = (n//6 +1) * info[0][0]
ans_mix = (n//6) * info[0][0]

info.sort(key = lambda x :(x[1], x[0]))
ans_mix += (n%6) * info[0][1]
ans_one = n*info[0][1]

print(min(ans_package, ans_mix, ans_one))