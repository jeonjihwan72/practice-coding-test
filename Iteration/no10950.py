# 문제 
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.(0 < A, B < 10)
'''

# 출력
'''
각 테스트 케이스마다 A+B를 출력한다.
'''

test_case_amount = int(input("테스트 케이스 개수를 입력: "))

test_case = []

for _ in range(test_case_amount):
    a, b = map(int, input("테스트 케이스 입력: ").split())
    test_case.append((a,b))
    
for case in test_case:
    print(f"{case[0]} + {case[1]} = {case[0]+case[1]}")