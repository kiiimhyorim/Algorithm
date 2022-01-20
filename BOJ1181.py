n = int(input())

string = []
for _ in range(n):
    string.append(input())
#중복 제거    
string = list(set(string))
#길이 -> 사전 순서로 정렬
string = sorted(string, key = lambda x:(len(x),x))

for s in string:
    print(s)