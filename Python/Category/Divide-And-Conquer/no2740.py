# 문제 
'''
N * M 크기의 행렬 A와 M * K 크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 행렬 A의 크기 N과 M이 주어진다.
둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 순서대로 주어진다.
그 다음 줄에는 행렬 B의 크기 M과 K가 주어진다.
이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다.
N과 M, 그리고 K는 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
'''

# 출력
'''
첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다.
행렬의 각 원소는 공백으로 구분한다.
'''
 
N, M1 = map(int, input().split())

matrix_01 = []

for _ in range(N):
    element = [int(x) for x in input().split()]
    matrix_01.append(element)

M2, K = map(int, input().split())

matrix_02 = []

for _ in range(M2):
    element = [int(x) for x in input().split()]
    matrix_02.append(element)

if M1 != M2:
    print("행렬 곱 불가")
    exit()

result = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M1):
            result[i][j] += matrix_01[i][k] * matrix_02[k][j]

print("======= 행렬 곱 출력 =======")
for row in result:
    print(" ".join(map(str, row)))