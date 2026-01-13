# 문제 
'''
오늘도 서준이는 병합 정렬 수업 조교를 하고 있다.
아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 서로 다른 양의 정수가 저장된 배열 A가 있다.
병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K번째 저장되는 수를 구해서 우리 서준이를 도와주자.

크기가 N인 배열에 대한 병합 정렬 의사 코드는 다음과 같다.

원본 링크 : https://www.acmicpc.net/problem/24060
'''

# 입력
'''
첫째 줄에 배열 A의 크기 N(5 <= N <= 500,000), 저장 횟수 K(1 <= K <= 10^8)가 주어진다.

다음 줄에 서로 다른 배열 A의 원소 A1, A2, ... , AN이 주어진다. (1 <= Ai <= 10^9)
'''

# 출력
'''
배열 A에 K번째 저장되는 수를 출력한다.
저장 횟수가 K보다 작으면 -1을 출력한다.
'''

import sys

def merge_sort(arr, tmp, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, tmp, left, mid)
        merge_sort(arr, tmp, mid + 1, right)
        merge(arr, tmp, left, mid, right)

def merge(arr, tmp, left, mid, right):
    global count, K, result
    i, j, t = left, mid + 1, left
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1
        count += 1
        if count == K:
            result = tmp[t - 1]
    
    while i <= mid:
        tmp[t] = arr[i]
        i += 1
        t += 1
        count += 1
        if count == K:
            result = tmp[t - 1]
    
    while j <= right:
        tmp[t] = arr[j]
        j += 1
        t += 1
        count += 1
        if count == K:
            result = tmp[t - 1]
    
    for i in range(left, right + 1):
        arr[i] = tmp[i]

# 입력 받기
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# 병합 정렬 수행
tmp = [0] * N
count = 0
result = -1
merge_sort(A, tmp, 0, N - 1)

# 결과 출력
print(result)

## chat gpt ###################