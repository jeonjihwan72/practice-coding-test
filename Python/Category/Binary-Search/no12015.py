# 문제 
'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10,20,10,30,20,50}인 경우에 가장 긴 증가하는 부분 수열은 A = {10,20,30,50}이고, 길이는 4이다.
'''

# 입력
'''
첫째 줄에 수열 A의 크기 N(1 <= N <= 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 <= Ai <= 1,000,000)
'''

# 출력
'''
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
'''

import bisect

def longest_increasing_subsequence(arr):
    sub = []
    
    for num in arr:
        pos = bisect.bisect_left(sub, num)  # num이 들어갈 위치 찾기
        if pos == len(sub):
            sub.append(num)  # 가장 큰 값이면 추가
        else:
            sub[pos] = num  # 적절한 위치에 교체
    
    return len(sub)

# 입력
N = int(input())
A = list(map(int, input().split()))

# 출력
print(longest_increasing_subsequence(A))