#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    /* 동적 메모리 할당 및 사용 방법 */
    int *pi;
    pi = (int *)malloc(sizeof(int)); // int형 변수의 크기만큼 메모리를 할당한다.
    if (pi == NULL)                  // 메모리를 할당받지 못한 경우
    {
        printf("동적 메모리 할당에 실패했습니다.");
        exit(1); // 프로그램을 종료한다.
    }
    *pi = 100; // 메모리에 100을 저장한다.
    printf("%d\n", *pi);
    free(pi); // 동적 메모리를 사용한 이후에는 메모리를 반환해줘야 한다.

    /* 동적 메모리를 활용한 문자열 관리 */
    char *pc = NULL;
    int i = 0;
    pc = (char *)malloc(100 * sizeof(char)); // 문자 100개를 저장할 수 있는 메모리를 할당한다.
    if (pc == NULL)
    {
        printf("동적 메모리 할당에 실패했습니다.");
        exit(1);
    }
    // pc가 가리키는 포인터를 1씩 증가시키면서 알파벳 소문자를 저장한다.
    for (i = 0; i < 26; i++)
    {
        *(pc + i) = 'a' + i;
    }
    *(pc + i) = 0;      // 마지막에 null(ASCII코드에서 0은 null을 의미) 문자를 저장한다.
    printf("%s\n", pc); // abcdefghijklmnopqrstuvwxyz
    free(pc);

    /* 동적 메모리를 활용한 배열 관리 */
    int *pi2, j;
    pi2 = (int *)malloc(5 * sizeof(int)); // int형 변수 5개를 저장할 수 있는 메모리를 할당한다.
    if (pi2 == NULL)
    {
        printf("동적 메모리 할당에 실패했습니다.");
        exit(1);
    }
    pi2[0] = 100; // 배열의 첫 번째 원소에 100을 저장한다.
    pi2[1] = 200;
    pi2[2] = 300;
    pi2[3] = 400;
    pi2[4] = 500;
    for (j = 0; j < 5; j++)
    {
        printf("%d\n", *(pi2 + j)); // 배열의 모든 원소를 출력한다.
    }
    free(pi2);

    return 0;
}