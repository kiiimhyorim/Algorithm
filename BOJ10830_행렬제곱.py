n, b = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def matrix_mul(mtx,origin_mtx):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            val = 0
            for k in range(n):
                result[i][j] += mtx[i][k] * origin_mtx[k][j]
                
            result[i][j] %= 1000
    return result


Binary = bin(b)[2:] #2진법으로 변환

#단위 행렬
identity_matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

#2진법 자릿수 만큼 제곱 & 제곱한 행렬 끼리 곱해줌
result = identity_matrix[:]
for i in range(len(Binary)):
    if Binary[-i-1] == '1':
        temp = matrix[:]
        while i != 0:
            temp = matrix_mul(temp, temp)
            i -= 1
        result = matrix_mul(result, temp)


for i in range(n):
    for j in range(n):
        print(result[i][j], end = ' ')
    print()