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
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for target in M:
    print(binary_search(N,target), end = ' ')