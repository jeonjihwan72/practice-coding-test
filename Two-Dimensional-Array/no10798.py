# 문제 
'''
아직 글을 모르는 영석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다.
이 장난감에 있는 글자들을 영어 대문자 'A'부터 'Z', 영어 소문자 'a'부터 'z', 숫자 0부터 9이다.
영석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다. 
다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다.
이런 식으로 다섯개의 단어를 만든다.
아래 그림 1은 영석이가 칠판에 붙여 만든 단어들의 예이다.

<그림 1>

한 줄의 단어는 글자들을 빈칸없이 연속으로 나열해서 최대 15개의 글자들로 이루어진다.
또한 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다.

심심해진 영석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.
세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다.
다음에 두 번째 글자들을 세로로 읽어 나간다.
위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다.
이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.
그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다.

그림 1에서 영석이가 세로로 읽은 순서대로 글자들을 공백없이 출력하면 다음과 같다.

Aa0aPAf985Bz1EhCz2W3D1gkD6x

칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.

원본 링크 : https://www.acmicpc.net/problem/10798
'''

# 입력
'''
총 다섯줄의 입력이 주어진다. 
각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸없이 연속으로 주어진다.
주어지는 글자는 영어 대문자 'A'부터 'Z', 영어 소문자 'a'부터 'z', 숫자 0부터 9 중 하나이다.
각 줄의 시작과 마지막에 빈칸은 없다.
'''

# 출력
'''
영석이가 세로로 읽은 순서대로 글자들을 출력한다.
이때, 글자들을 공백없이 연속해서 출력한다.
'''

# itertools 라이브러리 활용
from itertools import zip_longest

# 원소 입력받기
row_01 = list(input().strip())
row_02 = list(input().strip())
row_03 = list(input().strip())
row_04 = list(input().strip())
row_05 = list(input().strip())

# 행렬 합치기
letter_matrix = [row_01, row_02, row_03, row_04, row_05]

# 세로 순 문자 합하기
string = ''.join([''.join(filter(lambda x: x is not None, col)) for col in zip_longest(*letter_matrix, fillvalue=None)])

# 합친 문자 출력
print(string)

###########################################################################################################################

# # with Chat-GPT
# from itertools import zip_longest

# # 원소 입력받기
# rows = [list(input().strip()) for _ in range(5)]  # 문자열 그대로 리스트로 저장

# # 최대 열 크기 찾기
# max_col = max(len(row) for row in rows)

# # 세로로 읽어서 문자열 합치기 (빈칸을 무시)
# string = ''.join(''.join(filter(None, column)) for column in zip_longest(*rows, fillvalue=''))

# # 결과 출력
# print(string)



# itertools 라이브러리
'''
. 반복 관련 기능을 제공하는 표준 라이브러리
. 효율적인 반복 작업을 위한 함수 모음
. 대표적인 함수
    1. 무한 반복 : count(), cycle(), repeat()
    2. 조합과 순열 : permutations(), combinations()
    3. 길이가 다른 여러 리스트를 병렬로 묶음 : zip_longest()
    4. 기타 : groupby(), chain(), product() 등
'''

# zip_longest() 함수
'''
. 길이가 다른 여러 리스트를 가장 긴 리스트 기준으로 묶음
. 빈 자리는 fillvalue로 채움
. zip()과 달리 모든 요소를 끝까지 포함
'''