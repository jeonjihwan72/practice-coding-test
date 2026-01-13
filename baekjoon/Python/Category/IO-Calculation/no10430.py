# 문제 
'''
(A+B)%C는 ((A%C)+(B%C))%C와 같을까?
(AXB)%C는 ((A%C)X(B%C))%C와 같을까?
세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 A, B, C가 순서대로 주어진다. (2 <= A, B, C <= 10,000)
'''

# 출력
'''
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C)+(B%C))%C, 셋째 줄에 (AXB)%C, 넷째 줄에 ((A%C)X(B%C))%C를 출력한다.
'''

A, B, C = map(int, input("A, B, C를 입력: ").split())

result_01 = (A+B)%C
result_02 = ((A%C)+(B%C))%C
result_03 = (A*B)%C
result_04 = ((A%C)*(B%C))%C

print(result_01)
print(result_02)
print(result_03)
print(result_04)
print("---------------------------------------")
print("(A+B)%C는 ((A%C)+(B%C))%C와 같을까? : ", end='')
print(result_01 == result_02)
print("(AXB)%C는 ((A%C)X(B%C))%C와 같을까? : ", end='')
print(result_03 == result_04)