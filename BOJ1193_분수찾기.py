x = int(input())

line = 0
max_num = 0
while x > max_num:
    line +=1
    max_num += line
    
gap = max_num - x
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line - gap  #분모
    
print('{}/{}'.format(top,under))