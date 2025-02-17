# 문제 
'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

1. x: 정수 x를 스택에 넣는다. (1 <= X <= 100,000)
2. 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다.
   없다면 -1을 대신 출력한다.
3. 스택에 들어있는 정수의 개수를 출력한다.
4. 스택이 비어있으면 1, 아니면 0을 출력한다.
5. 스택에 정수가 있다면 맨 위의 정수를 출력한다.
   없다면 -1을 대신 출력한다.
'''

# 입력
'''
첫째 줄에 명령의 수 N이 주어진다. (1 <= N <= 1,000,000)

둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.

출력을 요구하는 명령은 하나 이상 주어진다.
'''

# 출력
'''
출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.
'''

N = int(input("N: "))

stack = []
top = -1

for _ in range(N):
   command_line = input().split()
   command = int(command_line[0])
   if command == 1:
      stack.append(int(command_line[1]))
      top += 1
      print(stack)
      print("================")
   elif command == 2:
      if top == -1:
         print(-1)
         print("================")
      else:
         data = stack[top]
         stack.remove(stack[top])
         print(data)
         print("================")
         top -= 1
   elif command == 3:
      print(len(stack))
      print("================")
   elif command == 4:
      if len(stack) == 0:
         print(1)
         print("================")
      else:
         print(0)
         print("================")
   elif command == 5:
      if top == -1:
         print(-1)
         print("================")
      else:
         print(stack[top])
         print("================")