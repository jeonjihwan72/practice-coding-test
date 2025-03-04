# 문제 
'''
준규가 가지고 있는 동전은 총 N 종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 N과 K가 주어진다. (1 <= N <= 10, 1 <= K <= 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 <= Ai <= 1,000,000, A1 = 1, i >= 2인 경우에 Ai는 A(i-1)의 배수)
'''

# 출력
'''
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
'''

N, K = map(int, input("N, K: ").split())

coin_val = []

for _ in range(N):
    coin = int(input("coin: "))
    coin_val.append(coin)

coin_val.sort(reverse=True)
coin_amount = 0

for i in range(0,N):
    if i == 0:
        coin_amount += K // coin_val[i]
    else:
        coin_amount += (K % coin_val[i-1]) // coin_val[i]
   
print("===================")     
print(f"최소 동전 개수: {coin_amount}")