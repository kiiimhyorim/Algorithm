m = int(input())
n = int(input())

result = []

def is_prime(x):
    if x < 2:
        return False 
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

for i in range(m,n+1):
    if is_prime(i):
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)