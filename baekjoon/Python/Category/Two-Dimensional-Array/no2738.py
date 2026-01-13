# 문제 
'''
N * M 크기의 두 행렬 A와 B가 주어졌을 떄, 두 행렬을 더하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 행렬의 크기 N과 M이 주어진다. 
둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
'''

# 출력
'''
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 
행렬의 각 원소는 공백으로 구분한다.
'''

N, M = map(int, input("N과 M을 입력: ").split())

A = []
B = []

for _ in range(N):
    row = list(map(int, input("A의 행 원소 입력: ").split()))
    A.append(row)
    
for _ in range(N):
    row = list(map(int, input("B의 행 원소 입력: ").split()))
    B.append(row)
    
sum_ = [[0 for _ in range(M)] for _ in range(N)]

for i in range(0, N):
    for j in range(0, M):
        sum_[i][j] = A[i][j] + B[i][j]

for i in range(0, N):
    for j in range(0, M):
        print(sum_[i][j], end=' ')
    print()