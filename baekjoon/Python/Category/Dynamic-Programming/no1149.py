# 문제 
'''
RGB 거리에는 집이 N개 있다.
거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 떄,
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

. 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
. N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
. i(2 <= i <= N-1)번의 집은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''

# 입력
'''
첫째 줄에 집의 수 N(2 <= N <= 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑을 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.
'''

# 출력
'''
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''

N = int(input())  # 집의 개수
cost = [list(map(int, input().split())) for _ in range(N)]  # 각 집의 색칠 비용

# DP 테이블 초기화
dp = [[0] * 3 for _ in range(N)]  # 최소 비용을 저장하는 DP 배열
trace = [[-1] * 3 for _ in range(N)]  # 이전 색깔의 인덱스를 저장하는 배열

# 첫 번째 집 초기화
dp[0] = cost[0]

# DP 수행
for i in range(1, N):
    for j in range(3):  # 현재 색 (빨강=0, 초록=1, 파랑=2)
        # 이전 집에서 선택 가능한 색 중 최소 비용 선택
        if j == 0:  # 현재 빨강
            min_index = 1 if dp[i - 1][1] < dp[i - 1][2] else 2
        elif j == 1:  # 현재 초록
            min_index = 0 if dp[i - 1][0] < dp[i - 1][2] else 2
        else:  # 현재 파랑
            min_index = 0 if dp[i - 1][0] < dp[i - 1][1] else 1

        dp[i][j] = cost[i][j] + dp[i - 1][min_index]  # 최솟값 선택
        trace[i][j] = min_index  # 이전 선택된 색 저장

# 최종 결과 출력
min_cost = min(dp[N - 1])  # 마지막 집의 최소 비용
min_color = dp[N - 1].index(min_cost)  # 최소 비용이 발생한 색깔 인덱스

print(min_cost)

# 색깔 순서 추적
color_order = []
idx = min_color
for i in range(N - 1, -1, -1):
    color_order.append(idx)
    idx = trace[i][idx]

color_order.reverse()  # 역순으로 저장했으므로 반대로 정렬

print("색칠 순서:", color_order)  # 0: 빨강, 1: 초록, 2: 파랑