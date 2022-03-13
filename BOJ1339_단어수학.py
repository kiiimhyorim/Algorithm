n = int(input())
words = []
for _ in range(n):
    words.append(input())
    
dic = {}
for word in words:
    m = len(word) - 1 #자릿수를 나타냄
    for i in range(len(word)):
        if word[i] not in dic:
            dic[word[i]] = 10**m
        else:
            dic[word[i]] += 10**m
        m -=1

value_list = sorted(dic.values(), reverse = True)

ans = 0
num = 9
for val in value_list:
    ans += val*num
    num-=1
    
print(ans)