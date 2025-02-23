# 문제 
'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

. 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열
'''

# 입력
'''
첫째 줄에 자연수 N과 M이 주어진다. (1 <= M <= N <= 8)
'''

# 출력
'''
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

def backtrack(n, m, sequence, used):
    if len(sequence) == m:  # 길이가 M이 되면 출력
        print(" ".join(map(str, sequence)))
        return

    for i in range(1, n + 1):
        if not used[i]:  # 중복 방지
            used[i] = True
            backtrack(n, m, sequence + [i], used)
            used[i] = False  # 백트래킹

# 입력 처리
N, M = map(int, input().split())
used = [False] * (N + 1)  # 숫자 사용 여부 체크

backtrack(N, M, [], used)
