# 문제 
'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10,20,10,30,20,50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10,20,10,30,20,50} 이고, 길이는 4이다
'''

# 입력
'''
첫째 줄에 수열 A의 크기 N(1 <= N <= 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 <= Ai <= 1,000)
'''

# 출력
'''
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
'''

# N = int(input("N: "))

# num_list = [int(x) for x in input().split()]

# current = num_list[0]

# temp = [current]

# for num in num_list:
#     if num > current:
#         temp.append(num)
#         current = num

# print(len(temp))

#############################################################

N = int(input())
num_list = list(map(int, input().split()))

dp = [1] * N  # 각 위치에서 최장 증가 부분 수열의 길이를 저장할 DP 배열

for i in range(N):
    for j in range(i):
        if num_list[j] < num_list[i]:  # 앞에 있는 값 중 작은 값 찾기
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # 가장 긴 길이 출력
