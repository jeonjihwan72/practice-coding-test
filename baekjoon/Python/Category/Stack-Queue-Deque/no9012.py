# 문제 
'''
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인'('와 ')'만으로 구성되어 있는 문자열이다. 
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
한 쌍의 괄호 기호로 된 "()" 문자열은 기본 VPS이라고 부른다.
만일 x가 VPS라면 이것을 하나의 괄호에 넣은 새로운 문자열 "(x)"도 VPS가 된다.
그리고 두 VPS x와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS가 된다.
예를 들어 "(())()"dhk "((()))"는 VPS이지만 "(())()))", 그리고 "(()"는 모두 VPS가 아닌 문자열이다.

여러분은 입력으로 주어진 괄호 문자열이 VPS인지 아닌지 판단해서 그 결과를 YES와 NO로 나타내어야 한다.
'''

# 입력
'''
입력 데이터는 표준 입력을 사용한다.
입력은 T개의 테스트 데이터로 주어진다.
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.
하나의 괄호 문자열의 길이는 2 이상 50 이하이다.
'''

# 출력
'''
출력은 표준 출력을 사용한다.
만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 "YES", 아니면 "NO"를 한 줄에 하나씩 차례대로 출력해야 한다.
'''

T = int(input())

results = []
for _ in range(T):
    string = input().strip()
    check = []
    top = -1
    
    for element in string:
        result = True
        if element == '(':
            check.append('(')
            top += 1
        elif element == ')':
            if top == -1:
                result = False
                break
            else:
                check.remove(check[top])
                top -= 1
        
    if result == True and len(check) == 0:
        results.append(True)
    else:
        results.append(False)

for result in results:
    if result == True:
        print("YES")
    else:
        print("NO")