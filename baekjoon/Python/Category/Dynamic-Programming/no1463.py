# 문제 
'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

# 입력
'''
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.
'''

# 출력
'''
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''

# 재귀 사용
def find_min_count(target, num, cnt):
    global min_cnt
    if num > target:
        return
    if num == target:
        min_cnt = min(cnt, min_cnt)
        return
    find_min_count(target, num*3, cnt+1)
    find_min_count(target, num*2, cnt+1)
    find_min_count(target, num+1, cnt+1)
    return min_cnt

N = int(input("N: "))
min_cnt = 999
find_min_count(N, 1, 0)

print(min_cnt)

################################################################

# DP 중 메모이제이션 사용
def find_min_count(target):
    # dp[i]는 i까지 도달하는 최소 횟수
    dp = [float('inf')] * (target + 1)  # 큰 값으로 초기화
    dp[1] = 0  # 시작 값, 1에서 시작하는데 횟수는 0
    
    for num in range(1, target + 1):
        # 3배로 가는 경우
        if num * 3 <= target:
            dp[num * 3] = min(dp[num * 3], dp[num] + 1)
        # 2배로 가는 경우
        if num * 2 <= target:
            dp[num * 2] = min(dp[num * 2], dp[num] + 1)
        # 1 더하는 경우
        if num + 1 <= target:
            dp[num + 1] = min(dp[num + 1], dp[num] + 1)

    return dp[target]

N = int(input("N: "))
result = find_min_count(N)
print(result)