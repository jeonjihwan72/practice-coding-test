// 문제 
/*
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
*/

// 입력
/*
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
*/

// 출력
/*
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
*/
#include <stdio.h>

int main() {
  int A, B, C;
  int result_1, result_2, result_3, result_4;
  
  printf("A, B, C를 공백을 두고 입력: \n");
  scanf("%d %d %d", &A, &B, &C);

  result_1 = (int)((A+B)%C);
  result_2 = (int)((A%C + B%C)%C);
  result_3 = (int)((A*B)%C);
  result_4 = (int)((A%C * B%C)%C);

  int result_list[4] = {result_1, result_2, result_3, result_4};
  
  for (int i=0; i<4; i++) {
    printf("%d\n", result_list[i]);
  }

  printf("================\n");
  printf("1번 식과 2번 식의 결과는 같다: %d\n", result_1 == result_2);
  printf("3번 식과 4번 식의 결과는 같다: %d\n", result_3 == result_4);

  return 0;
}