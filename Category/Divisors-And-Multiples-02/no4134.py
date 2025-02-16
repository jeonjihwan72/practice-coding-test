# 문제 
'''
정수 n(0 <= n <= 4*10^9)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 테스트 케이스의 개수가 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
'''

# 출력
'''
각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.
'''

N = int(input("N: "))

prime_list = []
for _ in range(N):
    target = int(input())
    while True:
        prime_eval = 0
        for i in range(1,target+1):
            if target % i == 0:
                prime_eval += 1
        
        if prime_eval == 2:
            prime_list.append(target)
            break
        
        target += 1

print("####### 결과 출력 #######")
for prime in prime_list:
    print(prime)