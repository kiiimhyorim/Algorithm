import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    info = []
    for _ in range(n):
        info.append(list(map(int, input().split())))

    info.sort(key=lambda x :(x[0], x[1])) # 서류성적 순위 순 정렬

    min_idx = 0 #면접 점수 순위 높은 인덱스
    cnt = 1 # 서류 1등은 통과이기 때문
    for i in range(1, n):
        if info[min_idx][1] > info[i][1]:
            min_idx = i
            cnt +=1

    print(cnt)