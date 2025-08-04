# 문제 
'''
1번부터 N번까지 N개의 풍선이 원형으로 놓여 있다.
i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다.
단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다.
각 풍선 안에는 종이가 하나 들어있고, 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다.
이 풍선들을 다음과 같은 규칙으로 터뜨린다.

우선, 제일 처음에는 1번 풍선을 터뜨린다.
다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다.
양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다.
이동할 때에는 이미 터진 풍선은 빼고 이동한다.

예를 들어 다섯 개의 풍선 안에 차례로 3,2,1,-3,-1이 적혀 있었다고 하자.
이 경우 3이 적혀 있는 1번 풍선, -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다. 
'''

# 입력
'''
첫째 줄에 자연수 N(1 <= N <= 1,000)이 주어진다.
다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다. 
종이에 0은 적혀있지 않다.
'''

# 출력
'''
첫째 줄에 터진 풍선의 번호를 차례로 나열한다.
'''

from collections import deque

def rotation_right(dq:deque, num):
    for _ in range(num):
        data = dq.pop()
        dq.appendleft(data)
    
def rotation_left(dq:deque, num):
    for _ in range(num):
        data = dq.popleft()
        dq.append(data)

dq = deque()

N = int(input("N: "))

# 추출된 원소의 인덱스 보관 리스트
result = []

# N의 범위에 1이 포함되어 map함수 사용 불가
balloon = input().split()
for i in range(0, N):
    # balloon 안의 원소를 (정수화된 원소, 자연수화된 인덱스) 형태의 튜플로 수정
    dq.append((int(balloon[i]), i+1))

for _ in range(N):
    data, index = dq.popleft()
    result.append(index)
    
    if not dq:  # 덱이 비었을 경우 반복문 탈출
        break
    
    if data < 0:
        rotation_right(dq,-data)    # 오른쪽으로 회전할 경우에는 해당 원소를 포함하지 않으므로 -1을 붙이지 않는다.
    else:
        rotation_left(dq, data-1)

for id in result:
    print(id, end=' ')