import heapq
import sys
input = sys.stdin.readline
n = int(input())
leftheap = []
rightheap = []

for _ in range(n):
    num = int(input())
    
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-num, num)) #최대힙
    else:
        heapq.heappush(rightheap, (num,num)) #최소힙
    
    # rightheap이 비어있지 않을 때
    # leftheap의 가장 큰 값이 rightheap의 가장 작은 값 보다 클 때
    # 자리 변경
    if rightheap and leftheap[0][1] > rightheap[0][0]:
        min_val = heapq.heappop(rightheap)[0]
        max_val = heapq.heappop(leftheap)[1]
        
        heapq.heappush(leftheap, (-min_val, min_val))
        heapq.heappush(rightheap, (max_val, max_val))
        
    print(leftheap[0][1])