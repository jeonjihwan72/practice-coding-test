# 문제 
'''
피보나치 수는 0과 1로 시작한다. 
0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
그 다음 2번째부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = F(n-1) + F(n-2) (n >= 2) 가 된다.

n = 17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 떄, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 n이 주어진다.
n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.
'''

# 출력
'''
첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.
'''

# Chat GPT's Answer
import sys

MOD = 1_000_000_007

def matrix_mult(A, B):
    """ 행렬 A와 B를 곱하고 MOD 연산을 적용 """
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]

def matrix_pow(mat, exp):
    """ 행렬 mat을 exp 제곱 (O(log n) 분할 정복) """
    res = [[1, 0], [0, 1]]  # 단위 행렬
    base = mat

    while exp:
        if exp % 2:
            res = matrix_mult(res, base)  # 홀수 차수일 때 현재 행렬 곱하기
        base = matrix_mult(base, base)  # 행렬 제곱
        exp //= 2

    return res

def fibonacci(n):
    """ 피보나치 수 F(n)을 행렬 거듭제곱을 이용해 구함 """
    if n == 0:
        return 0
    if n == 1:
        return 1

    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n-1)
    return result[0][0]  # F(n) 값 반환

# 입력 받기
n = int(sys.stdin.readline().strip())
print(fibonacci(n))

# np.dot() 함수 : NumPy에서 벡터 또는 행렬의 내적을 계산하는 함수
# 기본적인 역할
# 두 벡터의 내적 (dot product)
# 행렬 곱셈 (matrix multiplication)
# 스칼라 곱셈도 가능하지만, 주로 벡터와 행렬 연산에 사용됨

# 행렬 곱셈을 이용한 피보나치 수열
'''
[F(n) \ F(n-1)] = [1 1 \ 1 0][F(n-1) \ F(n-2)]

이 행렬 곱셈을 일반화하여 다음과 같이 피보나치 수열을 나타낸다.

[F(n) \ F(n-1)] = [1 1 \ 1 0]^(n-1) [F(1) \ F(0)]
'''