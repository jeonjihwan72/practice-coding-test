# 문제 
'''
시험 점수를 입력받아 
90 ~ 100점은 A, 
80 ~ 89점은 B, 
70 ~ 79점은 C, 
60 ~ 69점은 D, 
나머지 점수는 F를 출력하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
'''

# 출력
'''
시험 성적을 출력한다.
'''

while True:
    score = int(input("시험 점수를 입력: "))
    if score >= 0 and score <= 100:
        break
    print("범위를 벗어난 점수입니다.")

if 90 <= score and 100 >= score:
    print('A')
elif 80 <= score and 89 >= score:
    print('B')
elif 70 <= score and 79 >= score:
    print('C')
elif 60 <= score and 69 >= score:
    print('D')
else:
    print('F')