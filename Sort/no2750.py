# 문제 
'''
N개의 수가 주어졌을 때, 이를 오름차순으로 청렬하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 수의 개수 N(1 <= N <= 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다.
이 수는 절댓값이 1,000보다 작거나 같은 정수이다.
수는 중복되지 않는다.
'''

# 출력
'''
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

num_list = []

amount = int(input("수의 개수 입력: "))

for _ in range(amount):
    num = int(input())
    num_list.append(num)

# 내림차순 정렬
# num_list.sort(reverse=True)

# 오름차순 정렬
num_list.sort()

print("##### 결과 출력 #####")
for num in num_list :
    print(num)