# 문제 
'''
세준이는 크기가 N x N인 배열 A를 만들었다.
배열에 들어있는 수 A[i][j] = i x j 이다.
이 수를 일차원 배열 B에 넣으면 B의 크기는 N x N이 된다.
B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.
'''

# 입력
'''
첫째 줄에 배열의 크기 N이 주어진다.
N은 10^5보다 작거나 같은 자연수이다.
둘째 줄에 k가 주어진다.
k는 min(10^9, N^2)보다 작거나 같은 자연수이다.
'''

# 출력
'''
B[k]를 출력한다.
'''

def count_less_equal(x, N):
    count = 0
    for i in range(1, N + 1):
        count += min(x // i, N)
    return count

def find_kth_number(N, k):
    low, high = 1, N * N
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        if count_less_equal(mid, N) >= k:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer

# 입력
N = int(input())
k = int(input())

# 출력
print(find_kth_number(N, k))

# 이진 탐색을 활용한 k번째 값 찾는 원리
'''
- 직접 배열을 생성해 k번째 값을 찾을 경우 N값이 크면 오버플로우 발생한다.
- 이진 탐색을 활용하여 직접 k번재 수를 찾아가는 방법 채택

1. k번째 원소를 찾는 것은 '최소한 k개의 원소를 포함하는 가장 작은 값 x'를 찾는 것
    - 배열 B를 정렬한 상태에서 k번째 원소를 찾는 것은 
      배열 B에서 k개 이상의 원소를 가지는 가장 작은 수 x를 찾는 것과 동일

2. 특정값 x보다 작거나 같은 원소의 개수 구하기
    - 특정한 숫자 x가 주어졌을 때, 
      행렬 A 에서 x이하인 숫자가 몇 개인지 빠르게 구할 수 있다.
    
각 행을 보면, i번째 행에서 x이하인 값은 min(x/i, N)개 존재한다.
즉, x이하의 원소 개수는 sum(i=1~N)(min(x/i, N))

이 식을 사용하면 x보다 작거나 같은 원소가 몇 개인지 빠르게 계산할 수 있다.
'''

# 이진 탐색을 활용한 해결 방법
'''
1. 탐색 범위 설정
    - B 배열의 최소값은 1, 최대값은 N x N 이므로 초기 탐색 범위를 low = 1, high = N x N 으로 설정

2. 이진 탐색 진행
    - mid = (low + high) // 2를 설정
    - mid 이하의 숫자가 몇 개인지 계산
    - 만약 개수가 k 이상이면 high = mid - 1로 범위를 감소
    - 개수가 k 미만이면 low = mid + 1로 증가 (더 큰 값을 찾아야 함)

3. 탐색 종료 후, low가 k번째 원소가 됨
    - 탐색이 끝나면, low값이 B[k]가 된다
'''