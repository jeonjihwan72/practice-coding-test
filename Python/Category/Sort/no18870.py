# 문제 
'''
수직선 위에 N개의 좌표 x1, x2, ... , xn이 있다. 
이 좌표에 좌표 압축을 적용하려고 한다.

xi를 좌표 압축한 결과 xi'의 값은 xi > xj를 만족하는 서로 다른 좌표 xj의 개수와 같아야 한다.

x1, x2, ... , xn에 좌표 압축을 적용한 결과 x1', x2', ... , xn'를 출력해보자.
'''

# 입력
'''
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 x1, x2, ... , xn이 주어진다.
'''

# 출력
'''
첫째 줄에 x1', x2', ... , xn'을 공백 한 칸으로 구분해서 출력한다.
'''

N = int(input("N : "))

input_ = list(map(int, input().split()))

output = [0 for _ in range(N)]

for i in range(0, N):
    count = 0
    small_num = []
    for j in range(0, N):
        if input_[i] > input_[j] and input_[j] not in small_num:
            count += 1
            small_num.append(input_[j])
    output[i] = count

for smaller in output:
    print(smaller, end=' ')