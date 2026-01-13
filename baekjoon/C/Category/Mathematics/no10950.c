// 문제 
/*
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
*/

// 입력
/*
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
*/

// 출력
/*
각 테스트 케이스마다 A+B를 출력한다.
*/
#include <stdio.h>

int main() {
  int amount;
  int A, B;

  printf("테스트 케이스의 개수를 입력하시오: ");
  scanf("%d", &amount);
  int sum_list[amount];

  for (int i=0; i<amount; i++) {
    printf("%d 번째 계산: A와 B를 공백으로 구분하여 입력하시오.\n", i+1);
    scanf("%d %d", &A, &B);
    sum_list[i] = A + B;
  }

  for (int i=0; i<amount; i++) {
    printf("%d번째 결과: %d\n", i+1, sum_list[i]);
  }
    
  return 0;
}