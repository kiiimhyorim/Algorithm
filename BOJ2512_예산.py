import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
total = int(input())

start = 1
end = max(budget)

while start <= end:
    mid = (start + end) // 2
    check = 0
    for i in range(n):
        if budget[i] > mid:
            check += mid
        else:
            check += budget[i]

    if check <= total:
        start = mid + 1
    else:
         end = mid - 1

print(end)