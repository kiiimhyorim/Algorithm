import sys
input = sys.stdin.readline

n = int(input())
N = list(map(int, input().split()))
N.sort()
m = int(input())
M = list(map(int, input().split()))

def binary_search(arr, target):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0

for i in range(m):
    print(binary_search(N, M[i]))