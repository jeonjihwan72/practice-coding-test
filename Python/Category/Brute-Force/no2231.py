# 문제 
'''
어떤 자연수 N이 있을 떄, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
예를 들어, 245의 분해합은 256(= 245 + 2 + 4 + 5)이 된다. 
따라서 245는 256의 생성자가 된다.
물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다.
반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 떄, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 자연수 N(1 <= N <= 1,000,000)이 주어진다.
'''

# 출력
'''
첫째 줄에 답을 출력한다.
생성자가 없는 경우에는 0을 출력한다.
'''
import math

def length(num:int):
    # return int(math.log10(num)) + 1
    return len(str(num))

num = int(input())

digits = length(num)
start = max(1, num - 9*len(str(num)))
M = 0

for i in range(start,num):
    
    # digit_sum = 0
    # for j in range(0,digits):
    #     digit_sum += (i % pow(10,j+1)) // pow(10,j)
    digit_sum = sum(int(d) for d in str(i))
    
    if digit_sum + i == num:
        M = i
        break
    
print(M)

# def get_digit_sum(n):
#     return sum(int(d) for d in str(n))

# num = int(input())

# # 생성자 후보의 최소값: num - (9 * 자릿수 개수)부터 탐색
# start = max(1, num - 9 * len(str(num)))

# for i in range(start, num):
#     if i + get_digit_sum(i) == num:
#         print(i)
#         break
# else:
#     print(0)