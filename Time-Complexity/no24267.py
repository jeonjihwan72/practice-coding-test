# 문제 
'''
오늘도 서준이는 알고리즘의 수행시간 수업 조교를 하고 있다.
아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.

MenOfPassion 알고리즘은 다음과 같다.

원본 링크 : https://www.acmicpc.net/problem/24267
'''

# 입력
'''
첫째 줄에 입력의 크기 n(1 <= n <= 500,000)이 주어진다.
'''

# 출력
'''
첫째 줄에 코드1의 수행 횟수를 출력한다.

둘째 줄에 코드1의 수행횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다.
단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.
'''

##### 제공된 코드(수정 금지) #####

def MenOfPassion(A, n):
    sum_value = 0
    for i in range(n - 2):  # i는 0부터 n-3까지
        for j in range(i + 1, n - 1):  # j는 i+1부터 n-2까지
            for k in range(j + 1, n):  # k는 j+1부터 n-1까지
                sum_value += A[i] * A[j] * A[k]  # 코드1
    return sum_value

#################################

n = int(input("수행 횟수: "))

count = 0

for i in range(n - 2):  # i는 0부터 n-3까지
    for j in range(i + 1, n - 1):  # j는 i+1부터 n-2까지
        for k in range(j + 1, n):  # k는 j+1부터 n-1까지
            count += 1

print(f"수행된 횟수: {count}")
print(f"시간 복잡도 차수 : 3")