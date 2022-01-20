import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    x = int(input())
    if x ==0:
        result.pop()
    else:
        result.append(x)
        
print(sum(result))