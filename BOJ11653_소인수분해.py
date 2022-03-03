n = int(input())

while n > 1: 
    div = 2
    for i in range(div, n+1):
        if n % i ==0:
            n = n// i
            print(i)
            break