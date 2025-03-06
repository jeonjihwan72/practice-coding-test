# 문제 
'''
크기가 N*N인 행렬 A가 주어진다.
이때, A의 B제곱을 구하는 프로그램을 작성하시오.
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.
'''

# 입력
'''
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 <= N <= 5, 1 <= B <= 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다.
행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.
'''

# 출력
'''
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
'''

def matrix_mult(A, B, N):
    """ 행렬 A와 B를 곱한 후, 각 원소를 1000으로 나눈 나머지 값을 반환 """
    result = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= 1000  # 모듈러 연산 적용

    return result

def matrix_pow(A, B, N):
    """ 행렬 A를 B제곱한 결과를 반환 (분할 정복) """
    if B == 1:  # B=1이면 A를 1000으로 나눈 나머지를 반환
        return [[A[i][j] % 1000 for j in range(N)] for i in range(N)]
    
    half = matrix_pow(A, B // 2, N)  # A^(B//2) 계산
    half = matrix_mult(half, half, N)  # (A^(B//2))^2 계산
    
    if B % 2:  # B가 홀수인 경우 A를 한 번 더 곱함
        return matrix_mult(half, A, N)
    else:
        return half

# 입력 받기
N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 행렬 거듭제곱 계산
result = matrix_pow(matrix, B, N)

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))