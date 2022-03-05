import sys
input = sys.stdin.readline
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort(reverse = True)

result = []
for cnt in range(1, n + 1):
    w = cnt * rope[i-1]
    result.append(w)

print(max(result))