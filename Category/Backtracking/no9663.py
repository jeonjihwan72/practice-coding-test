# 문제 
'''
N-Queen 문제는 크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 N이 주어진다. (1 <= N < 15)
'''

# 출력
'''
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''

# def queen(n, line, chess):
#     global count
#     if line == n:
#         count += 1
#         return
    
#     for i in range(0, n):
#         if chess[line][i] == True:
            

# N = int(input("N: "))

# chess = [[True for _ in range(N)] for _ in range(N)]
# count = 0

# queen(N, 0, chess)

# print(count)

def solve_n_queens(n):
    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or \
               board[prev_row] - prev_row == col - row or \
               board[prev_row] + prev_row == col + row:
                return False
        return True
    
    def backtrack(row):
        if row == n:
            nonlocal count
            count += 1
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    
    board = [-1] * n
    count = 0
    backtrack(0)
    return count

N = int(input())
print(solve_n_queens(N))
