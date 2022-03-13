num = input()

zero_list = num.split('0')
one_list = num.split('1')

zero_cnt = 0
one_cnt = 0

for zero in zero_list:
    if len(zero)>0:
        zero_cnt +=1
        
for one in one_list:
    if len(one)>0:
        one_cnt +=1
        
print(min(zero_cnt, one_cnt))