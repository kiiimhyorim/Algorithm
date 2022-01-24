import math
import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
    
# 산술평균
print(round(sum(num)/n))

#중앙값
num.sort()
print(num[n//2])

#최빈값
dic = {}
for i in range(len(num)):
    if num[i] not in dic.keys():
        dic[num[i]] = 1
    else:
        dic[num[i]]+=1
dic = sorted(dic.items())
dic.sort(key = lambda x: (x[1],-x[0]), reverse = True)

if n >1:
    if dic[0][1] == dic[1][1]: #최빈값 2개 이상
        print(dic[1][0])
    else:
        print(dic[0][0])
else:
    print(dic[0][0])

#범위
print(num[-1] - num[0]) #정렬했으므로 양끝에 최소,최대