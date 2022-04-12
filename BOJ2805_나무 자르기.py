import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)
while start <= end:
    mid = (start + end) // 2
    check = 0
    for tree in trees:
        if tree > mid:
            check += (tree - mid)

    if check >= m: #원하는 양보다 많이 잘렸으면
        start = mid + 1
    else:
        end = mid - 1

print(end)