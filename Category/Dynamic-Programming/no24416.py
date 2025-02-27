# 문제 
'''
오늘도 서준이는 동적 프로그래밍 수업 조교를 하고 있다.
아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

오늘은 n의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다.
재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자.
아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

피보나치 수 재귀호출 의사코드는 다음과 같다.

피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

원본 링크 : https://www.acmicpc.net/problem/24416
'''

# 입력
'''
첫째 줄에 n(5 <= n <= 40)이 주어진다.
'''

# 출력
'''
코드1 코드2 실행 횟수를 한 줄에 출력한다.
'''

def fib(n) :
    global count_fib
    if n == 1 or n == 2:
        count_fib += 1
        return 1    # 코드 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global count_fibonacci
    f = [1, 1]
    for i in range(2,n):
        count_fibonacci += 1
        f.append(f[i-1]+f[i-2]) # 코드 2
    return f[n-1]
    
f = []    
count_fib = 0
count_fibonacci = 0

N = int(input("N: "))

fib(N)
fibonacci(N)

print(count_fib, count_fibonacci)