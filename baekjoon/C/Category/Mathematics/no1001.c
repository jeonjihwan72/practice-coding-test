// 문제 
/*
두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
*/

// 입력
/*
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
*/

// 출력
/*
첫째 줄에 A-B를 출력한다.
*/

#include <stdio.h>

int main() {
  int A, B, C; // 변수 타입 선언

  printf("A와 B를 입력하시오.\n");
  scanf("%d %d", &A, &B); // 사용자로 부터 A와 B를 포맷팅 형식으로 입력 받음
  C = A - B; // C에 대하여 정의
  printf("%d", C);

  return 0;
}