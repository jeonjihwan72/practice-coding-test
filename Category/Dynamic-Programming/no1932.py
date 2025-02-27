# 문제 
'''
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1이상 500이하이다.
삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0이상 9999이하이다.

원본 링크 : https://www.acmicpc.net/problem/1932
'''

# 입력
'''
첫째 줄에 삼각형의 크기 n(1 <= n <= 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
'''

# 출력
'''
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
'''

# # 재귀 호출 (브루트 포스(완전 탐색) 알고리즘 사용)
# def search_max(N, sum_, loc, idx, map):
#     global sum_list
#     if loc == N:
#         sum_list.append(sum_)
#         return
#     search_max(N, sum_ + map[loc][idx], loc+1, idx, map)
#     search_max(N, sum_ + map[loc][idx], loc+1, idx+1, map)

# sum_list = []

# N = int(input("N: "))

# tri = []
# for _ in range(N):
#     num = [int(x) for x in input().split()]
#     tri.append(num)

# search_max(N, 0, 0, 0, tri)

# print(max(sum_list))

# 동적 계산법(DP) 사용

N = int(input("N: "))

tri = []
for _ in range(N):
    num = [int(x) for x in input().split()]
    tri.append(num)

# DP 테이블 초기화
dp = [[0] * (i + 1) for i in range(N)]
dp[0][0] = tri[0][0]  # 맨 위층 값 초기화

# Bottom-Up 방식으로 DP 진행
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

# 마지막 행에서 최댓값 출력
print(max(dp[N-1]))
