# 문제 
'''
NxN 크기의 행렬로 표현되는 종이가 있다.
종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다.
우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
2. (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.

이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 N(1 <= N <= 3^7, N은 3^k꼴)이 주어진다.
다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.
'''

# 출력
'''
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
'''

def square(x, y, size):
    global paper, minus, plus, zero
    part_color = paper[x][y]
    
    all_same = True
    for i in range(x,x+size):
        for j in range(y,y+size):
            if part_color != paper[i][j]:
                all_same = False
                break
        if not all_same:
            break
    
    if all_same:
        if part_color == -1:
            minus += 1
        elif part_color == 0:
            zero += 1
        elif part_color == 1:
            plus += 1
        return 
    
    if size == 1:
        return
    
    new_size = size // 3
    if new_size == 0:
        return
    
    first = new_size
    second = new_size *2
    
    square(x, y, new_size)
    square(x+first, y, new_size)
    square(x+second, y, new_size)
    square(x, y+first, new_size)
    square(x, y+second, new_size)
    square(x+first, y+first, new_size)
    square(x+first, y+second, new_size)
    square(x+second, y+first, new_size)
    square(x+second, y+second, new_size)
    
N = int(input("N: "))
paper = [[int(x) for x in input().split()] for _ in range(N)]

minus, zero, plus = 0, 0, 0

square(0,0,N)

print("======= 결과 출력 =======")
print(f"- : {minus}")
print(f"0 : {zero}")
print(f"+ : {plus}")