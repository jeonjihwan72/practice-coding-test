# 문제 
'''
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 정수 N(1 <= N <= 10,000,000)이 주어진다.
'''

# 출력
'''
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다.
N이 1인 경우 아무것도 출력하지 않는다.
'''

import sys

def prime_factorization(n):
    if n == 1:
        return

    # 2부터 시작하여 n의 소인수를 찾음
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            print(factor)
            n //= factor
        factor += 1

    # 남은 값이 1보다 크다면 그것도 소수이므로 출력
    if n > 1:
        print(n)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())  # 입력 받기
    prime_factorization(n)