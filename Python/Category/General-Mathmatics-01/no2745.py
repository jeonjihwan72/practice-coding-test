# 문제 
'''
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다.
이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A : 10, B : 11, ... , Y : 34, Z : 35
'''

# 입력
'''
첫째 줄에 N과 B가 주어진다. (2 <= B <= 36)
B 진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.
'''

# 출력
'''
첫째 줄에 B진법 수 N을 10진법으로 출력한다.
'''

alpha = [chr(i) for i in range(65,91)]
over_num = [i for i in range(10,36)]

decimal = {alphabet:decimal_num for alphabet, decimal_num in zip(alpha, over_num)}

pre_num, N = input().split()
N = int(N)

digits = len(pre_num)

fin_num = 0

for i in range(1, digits+1):
    if pre_num[i-1].isdigit() :
        a = int(pre_num[i-1])
        fin_num += a * pow(N, digits - i)
    else :
        a = decimal[pre_num[i-1]]
        fin_num += a * pow(N, digits - i)

print(fin_num)