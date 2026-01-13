# 문제 
'''
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → ...과 같은 지그재그 순서로 
차례대로 1번, 2번, 3번, 4번, 5번, ... 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

원본 링크 : https://www.acmicpc.net/problem/1193
'''

# 입력
'''
첫째 줄에 X(1 <= X <= 10,000,000)가 주어진다.
'''

# 출력
'''
첫째 줄에 분수를 출력한다.
'''

def fibonacci(num):
    if num == 0:
        return 0    
    if num == 1:
        return 1
    return fibonacci(num-1) + num
    
def summation(num):
    count = 1
    while True:
        if fibonacci(count) >= num:
            result = (count + 1, count%2, num - fibonacci(count-1))
            break
        count += 1
    return result

order = int(input("분수 순서: "))

temp_tuple = summation(order)

odd = None

if temp_tuple[1] == 1:
    odd = True
else :
    odd = False

index = temp_tuple[2]

denominator_sum = temp_tuple[0]
fraction = None

if odd:
    fraction = [f'{denominator_sum-i}/{i}' for i in range(1,denominator_sum)]
else:
    fraction = [f'{i}/{denominator_sum-i}' for i in range(1,denominator_sum)]

print(fraction[index-1])