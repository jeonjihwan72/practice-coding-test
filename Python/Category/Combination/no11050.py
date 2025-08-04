# 문제 
'''
자연수 N과 정수 K가 주어졌을 때, 이항 계수 NCK를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 N과 K가 주어진다. (1<=K<=10, 0<=K<=N)
'''

# 출력
'''
nCk를 출력한다. 
'''

N, K = map(int, input("N, K: ").split())

molecular = 1

denominator = 1

for i in range(N,N-K,-1):
    molecular *= i

for i in range(1,K+1):
    denominator *= i

print(molecular//denominator)