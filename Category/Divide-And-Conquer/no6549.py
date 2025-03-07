# 문제 
'''
히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다.
각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다.
예를 들어, 왼쪽 그림은 높이가 2,1,4,5,1,3,3이고 너비가 1인 정사각형으로 이루어진 히스토그램이다.

히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

원본 링크 : https://www.acmicpc.net/problem/6549
'''

# 입력
'''
입력은 테스트 케이스 여러 개로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다. (1 <= n <= 100,000)
그 다음 n개의 정수 h1, ... , hn (0 <= h1 <= 1,000,000,000)가 주어진다.
이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다.
모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.
'''

# 출력
'''
각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.
'''

# Chat GPT's Answer
# Not Success

def largest_rectangle(histogram):
    stack = []
    max_area = 0
    n = len(histogram)

    for i in range(n):
        while stack and histogram[stack[-1]] > histogram[i]:
            height = histogram[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack:
        height = histogram[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

while True:
    values = list(map(int, input().split()))
    if values[0] == 0:  # 첫 번째 값이 0이면 종료
        break
    print(largest_rectangle(values[1:]))  # 첫 번째 값(직사각형 개수)은 제외하고 전달
