# 문제 
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''

# 입력
'''
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
'''

# 출력
'''
각 테스트 케이스마다 A+B를 출력한다.
'''

# 테스트 케이스의 개수에 대해서는 별도로 제시되어있지 않아 예제와 같이 5개로 고정
test_case_amount = 5

test_case = []

for _ in range(test_case_amount):
    a, b = map(int, input("A와 B를 입력: ").split())
    test_case.append((a, b))
    
for case in test_case:
    print(case[0] + case[1])