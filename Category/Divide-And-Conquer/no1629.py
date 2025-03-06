# 문제 
'''
자연수 A를 B번 곱한 수를 알고 싶다.
단, 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다.
A, B, C는 모두 2,147,483,647 이하의 자연수이다.
'''

# 출력
'''
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
'''

# # A, B의 값이 커지면 오버플로우 발생
# A, B, C = map(int, input().split())
# print((A ** B) % C)

'''==============================================================='''
A, B, C = map(int, input("A, B, C: ").split())

def exponentiation(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    
    if b % 2 == 0:
        half = exponentiation(a, b // 2, c)
        return (half * half) % c
    else:
        half = exponentiation(a, b - 1, c)
        return (half * a) % c
    
print(exponentiation(A, B, C))

# 분할 정복을 이용한 거듭제곱 (빠른 거듭제곱, Exponentiation by Squaring)
'''
(A^B) mod C = 
| (((A^(B//2)) mod C) ^ 2) mod C    (B가 짝수일 때)
| (((A^(B-2)) mod C) * A) mod C    (B가 홀수일 때)
'''
# 재귀를 이용하여 계산하므로 큰 수 A와 B의 곱으로 오버플로우가 발생하지 않고
# 시간 복잡도가 O(log B)로 줄어든다.