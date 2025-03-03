# 문제 
'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M x N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
지민이는 이 보드를 잘라서 K x K 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색을 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 K x K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 K x K 크기는 아무데서나 골라도 된다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 정수 N, M, K가 주어진다.
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다.
B는 검은색이며, W는 흰색이다.
'''

# 출력
'''
첫째 줄에 지민이가 잘라낸 K x K 보드를 체스판으로 만들기 위해 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
'''
def odd_checker(x,y):
    if x+y % 2 == 0:
        return False
    else:
        return True

def chess_maker(target):
    global K
    way1, way2 = 0, 0
    
    for i in range(0,K):
        for j in range(0,K):
            if odd_checker(i,j):
                if target[i][j] == 'W':
                    way1 += 1
            else:
                if target[i][j] == 'B':
                    way1 += 1
    
    for i in range(0,K):
        for j in range(0,K):
            if odd_checker(i,j):
                if target[i][j] == 'B':
                    way2 += 1
            else:
                if target[i][j] == 'W':
                    way2 += 1
    
    count = min(way1, way2)
    return count

N, M, K = map(int, input("N, M, K: ").split())

table = []
for _ in range(N):
    temp = list(input().strip())
    table.append(temp)

count_list = []
for i in range(0, N-K+1):
    for j in range(0, M-K+1):
        # 2차원 슬라이싱이 바로 되지 않기 때문에 
        # 2번 슬라이싱하는 형태로 리스트 생성
        temp = [row[j:j+K] for row in table[i:i+K]]
        count_list.append(chess_maker(temp))
        
print("=========================")
print(min(count_list))