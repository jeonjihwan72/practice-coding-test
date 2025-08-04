# 문제 
'''
10진법 수 N이 주어진다.
이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다.
이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A : 10, B : 11, ... , F : 15, ... , Y : 34, Z : 35
'''

# 입력
'''
첫째 줄에 N과 B가 주어진다.
(2 <= B <= 36) N은 10억보다 작거나 같은 자연수이다.
'''

# 출력
'''
첫째 줄에 10진법 수 N을 B진법으로 출력한다.
'''

alpha = [chr(i) for i in range(65,91)]
over_num = [i for i in range(10,36)]

decimal = {decimal_num:alphabet for alphabet, decimal_num in zip(alpha, over_num)}

decimal_num, N = map(int, input("10진수, N을 입력: ").split())

fin_list = []
temp = decimal_num

while True:
    
    if temp // N == 0:
        fin_list.append(temp % N)
        break
    
    fin_list.append(temp % N)
    temp = temp // N

fin_num = ''

for num in fin_list:
    if num < 10 :
        fin_num += f'{num}'
    else:
        fin_num += decimal[num]

print(fin_num)