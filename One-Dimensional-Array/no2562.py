# 문제 
'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값을 85이고, 이 값은 8번째 수이다.
'''

# 입력
'''
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100보다 작다.
'''

# 출력
'''
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
'''

num_list = []

for i in range(1, 10):
    num = int(input(f"{i}번째 수 입력: "))
    num_list.append(num)

maximum = 0
maximum_index = None    

for i in range(0,9):
    if maximum < num_list[i]:
        maximum = num_list[i]
        maximum_index = i

print(f"최댓값은 {maximum} 입니다.")
print(f"최댓값은 {maximum_index+1} 번째에 있습니다.")