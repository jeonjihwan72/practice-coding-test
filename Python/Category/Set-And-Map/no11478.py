# 문제 
'''
문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

예를 들어, ababc의 부분 문자열은 

a,b,a,b,c,ab,ba,ab,bc,aba,bab,abc,abab,babc,ababc가 있고,

서로 다른 것의 개수는 12개이다.
'''

# 입력
'''
첫째 줄에 문자열 S가 주어진다.
S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.
'''

# 출력
'''
첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.
'''

string = list(input().strip())

L = len(string)

element_list = []
for i in range(1,L+1):              # i는 문자 개수
    for j in range(0,L-i+1):        # j는 문자 시작 지점
        temp = ''
        for k in range(0,i):        # k는 범위에 맞게 리스트를 훑으며 문자를 추가함
            temp += string[j+k]
        element_list.append(temp)

print(len(set(element_list)))