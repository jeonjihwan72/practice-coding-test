// 문제 
/*
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
*/

// 입력
/*
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
*/

// 출력
/*
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
*/
#include <stdio.h>

int main() {
  int A, B; // 변수 타입 선언

  printf("A와 B를 공백을 두고 입력하시오.\n");
  scanf("%d %d", &A, &B);
  
  printf("\n%d", A+B);
  printf("\n%d", A-B);
  printf("\n%d", A*B);
  printf("\n%d", A/B);  // '/'를 사용했을 때 변수의 타입에 따라 정수형(몫)·실수형(나눗셈)이 결정된다.
  printf("\n%d", A%B); 
  /*
  
  포맷팅에서의 타입별 서식 지정자(format specifier)

  1. 부호 있는 10진수 : %d  (int)
  2. 부호 있는 10진수 : %i  (int)
  3. 부호 없는 10진수 : %u  (unsigned int))
  4. 8진수 : %o  (unsigned int)
  5. 16진수(소문자) : %x  (unsigned int)
  6. 16진수(대문자) : %X  (unsigned int)
  7. 부호 있는 10진수 : %hd  (short → int 승격)
  
  */
  
  return 0;
}