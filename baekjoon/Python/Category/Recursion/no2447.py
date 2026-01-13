# 문제 
'''
재귀적인 패턴으로 별을 찍어보자. 
N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N x N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3) x (N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
예를 들어, 크기 27의 패턴은 예제 출력 1과 같다.
'''

# 입력
'''
첫째 줄에 N이 주어진다.
N은 3의 거듭제곱이다.
즉 어떤 정수 k에 대해 N=3^k이며, 이때 1 <= k < 8이다.
'''

# 출력
'''
첫째 줄부터 N번째 줄까지 별을 출력한다.
'''

def draw_star(x, y, size):
    if size == 1:
        return  # 더 이상 나눌 수 없으면 종료

    new_size = size // 3  # 작은 패턴 크기

    # 가운데 공백 채우기
    for i in range(x + new_size, x + 2 * new_size):
        for j in range(y + new_size, y + 2 * new_size):
            stars[i][j] = " "

    # 9개 영역을 재귀적으로 처리
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue  # 가운데는 이미 공백이므로 건너뜀
            draw_star(x + i * new_size, y + j * new_size, new_size)

# 입력 받기
N = int(input().strip())  # 3^k 형태의 N을 입력 받음

# N x N 크기의 별 패턴을 초기화
stars = [["*"] * N for _ in range(N)]

# 재귀적으로 패턴 만들기
draw_star(0, 0, N)

# 결과 출력
for row in stars:
    print("".join(row))
