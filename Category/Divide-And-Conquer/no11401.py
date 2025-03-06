# 문제 
'''
자연수 N과 정수 K가 주어졌을 때 이항 계수 C(N,K)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 N과 K가 주어진다. (1 <= N <= 4,000,000, 0 <= K <= N)
'''

# 출력
'''
C(N,K)를 1,000,000,007로 나눈 나머지를 출력한다.
'''

MOD = 1000000007

def mod_inv(a, m):
    return pow(a, m - 2, m)  # 페르마의 소정리

def solve(N, K):
    # 팩토리얼과 역원 미리 계산
    fact = [1] * (N + 1)
    inv = [1] * (N + 1)
    
    # 팩토리얼 계산
    for i in range(2, N + 1):
        fact[i] = fact[i-1] * i % MOD
    
    # 역원 계산
    inv[N] = mod_inv(fact[N], MOD)
    for i in range(N - 1, 0, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD
    
    # C(N, K) 계산
    result = (fact[N] * inv[K] % MOD) * inv[N - K] % MOD
    return result

# 입력
N, K = map(int, input().split())

# 결과 출력
print(solve(N, K))

# 페르마의 소정리 (기호를 주석으로 작성 불가하여 찾아보기)