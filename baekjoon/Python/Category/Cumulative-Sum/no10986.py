# 문제 
'''
수 N개 A1, A2, ... , AN 이 주어진다.
이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

즉, Ai + ... + Aj (i <= j)의 합이 M으로 나누어 떨어지는 (i,j) 쌍의 개수를 구해야 한다.
'''

# 입력
'''
첫째 줄에 N과 M이 주어진다. (1 <= N <= 10^6, 2 <= M <= 10^3)
둘째 줄에 N개의 수 A1, A2, ... , AN이 주어진다. (0 <= Ai <= 10^9)
'''

# 출력
'''
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.
'''

N, M = map(int, input("N, M: ").split())

num_list = [int(x) for x in input().split()]

count = 0
for i in range(0,N):
    sum_ = 0
    for j in range(i,N):
        sum_ += num_list[j]
        if sum_ % M == 0:
            count += 1

print(count)