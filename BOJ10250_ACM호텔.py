import math
t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    
    if n % h ==0:
        floor = h
    else:
        floor = n % h
        
    room = math.ceil(n/h)
    if len(str(room)) == 1:
        print(str(floor)+'0'+str(room))
    else:
        print(str(floor) + str(room))