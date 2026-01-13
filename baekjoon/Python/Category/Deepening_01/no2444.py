# 문제 
'''
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
'''

# 입력
'''
첫째 줄에 N(1 <= N <= 100)이 주어진다.
'''

# 출력
'''
첫째 줄부터 2XN-1번째 줄까지 차례대로별을 출력한다.
'''

N = int(input("N을 입력: "))

total_line = 2 * N - 1

count_star = 1

for i in range(1, total_line+1):
    printing_star = '*' * count_star
    print(f"{printing_star:^{total_line}}")
    
    if i < total_line / 2:
        count_star += 2
    else:
        count_star -= 2