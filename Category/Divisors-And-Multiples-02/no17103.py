# 문제 
'''
. 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.

짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다.
짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자.
두 소수의 순서만 다른 것은 같은 파티션이다.
'''

# 입력
'''
첫째 줄에 테스트 케이스의 개수 T(1 <= T <= 100)가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 <= N <= 1,000,000을 만족한다.
'''

# 출력
'''
각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.
'''

import math

def eval_prime(num):
    if num < 2:
        return False  # 1 이하는 소수가 아님

    divisor_count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_count += 1  # 작은 약수
            if i != num // i:
                divisor_count += 1  # 큰 약수

            if divisor_count > 2:  # 소수가 아니면 바로 종료
                return False
    return True

def odd_check(num):
    if num % 2 == 0:
        return False
    else:
        return True

T = int(input("T: "))

results = []
for _ in range(T):
    N = int(input("N: "))
    prime = []
    count = 0
    
    for i in range(2,N):
        if eval_prime(i):
            prime.append(i)
    
    for i in prime:
        for j in prime:
            if i + j == N:
                count += 1
    
    if odd_check(count):
        result_count = count // 2 + 1
    else:
        result_count = count // 2
    
    results.append(result_count)

print("##### 결과 출력 #####")
for result in results:
    print(result)