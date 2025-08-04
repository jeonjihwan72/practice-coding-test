# 문제 
'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 <= M <= N <= 1,000,000)
M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
'''

# 출력
'''
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''

M, N = map(int, input("M, N: ").split())

prime_list = []
for num in range(M,N+1):
    prime_eval = 0
    for i in range(1,num+1):
        if num % i == 0:
            prime_eval += 1
    if prime_eval == 2:
        prime_list.append(num)

print("####### 결과 출력 #######")
for prime in prime_list:
    print(prime)