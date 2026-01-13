// 문제 
/*
두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
*/

// 입력
/*
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
*/

// 출력
/*
첫째 줄에 A×B를 출력한다.
*/

#include <stdio.h>

int main() {
  int A, B, mult; // 변수 타입 선언

  printf("A와 B를 공백을 두고 입력하시오.\n");
  scanf("%d %d", &A, &B);
  mult = A * B;

  printf("%d", mult);
  
  return 0;
}