# 문제 
'''
분수 A/B는 분자가 A, 분모가 B인 분수를 의미한다.
A와 B는 모두 자연수라고 하자.

두 분수의 합 또는 분수로 표현할 수 있다.
두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성하시오.
기약분수란 더 이상 약분되지 않는 분수를 의미한다.
'''

# 입력
'''
첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다.
입력되는 네 자연수는 모두 30,000 이하이다.
'''

# 출력
'''
첫째 줄에 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 빈 칸을 사이에 두고 순서대로 출력한다.
'''
import math

num01 = list(map(int, input("분자, 분모: ").split()))
num02 = list(map(int, input("분자, 분모: ").split()))

temp_sum = [num01[1]*num02[0]+num01[0]*num02[1], num01[1]*num02[1]]
sum = None
GCD = math.gcd(temp_sum[0], temp_sum[1])
if GCD != 1:
    sum = [temp_sum[0]//GCD, temp_sum[1]//GCD]
else :
    sum = temp_sum

for element in sum:
    print(element, end=' ')