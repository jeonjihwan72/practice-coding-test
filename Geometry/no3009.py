# 문제 
'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
'''

# 입력
'''
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
'''

# 출력
'''
직사각형의 네 번째 점의 좌표를 출력한다.
'''

dot_loc = []

for _ in range(3):
    x, y = map(int, input().split())
    dot_loc.append((x,y))

first = pow(dot_loc[0][0] - dot_loc[1][0],2) + pow(dot_loc[0][1] - dot_loc[1][1],2)
second = pow(dot_loc[1][0] - dot_loc[2][0],2) + pow(dot_loc[1][1] - dot_loc[2][1],2)
third = pow(dot_loc[0][0] - dot_loc[2][0],2) + pow(dot_loc[0][1] - dot_loc[2][1],2)

if first == max([first, second, third]):
    mid = ((dot_loc[0][0]+dot_loc[1][0])/2, (dot_loc[0][1]+dot_loc[1][1])/2)
    another = (mid_+(mid_-dot) for mid_, dot in zip(mid, dot_loc[2]))
elif second == max([first, second, third]):
    mid = ((dot_loc[1][0]+dot_loc[2][0])/2, (dot_loc[1][1]+dot_loc[2][1])/2)
    another = (mid_+(mid_-dot) for mid_, dot in zip(mid, dot_loc[0]))
elif third == max([first, second, third]):
    mid = ((dot_loc[0][0]+dot_loc[2][0])/2, (dot_loc[0][1]+dot_loc[2][1])/2)
    another = (mid_+(mid_-dot) for mid_, dot in zip(mid, dot_loc[1]))
    
for loc in another:
    print(loc, end=' ')