#include <stdio.h>

int main(void)
{
    int x;
    scanf("%d", &x); // 입력을 받아서 x에 저장

    char o;
    int a, b;
    while (1)
    {
        printf("수식을 입력하세요: ");
        scanf("%d %c %d", &a, &o, &b); // 입력을 받아서 a, o, b에 저장
        if (o == '+')
            printf("%d\n", a + b); // o가 +이면 a와 b를 더한 값을 출력
        else if (o == '-')
            printf("%d\n", a - b); // o가 -이면 a와 b를 뺀 값을 출력
        else if (o == '*')
            printf("%d\n", a * b); // o가 *이면 a와 b를 곱한 값을 출력
        else if (o == '/')
            printf("%d\n", a / b); // o가 /이면 a와 b를 나눈 값을 출력

        getchar();                                    // 입력 버퍼에 남아있는 개행 문자를 제거
        printf("프로그램을 종료하시겠습니까? (y/n)"); // 프로그램을 종료할 것인지 물어봄
        scanf("%c", &o);                              // 입력을 받아서 o에 저장
        if (o == 'y')
            break; // 만약 o가 y이면 반복문을 빠져나감
        else if (o == 'n')
            continue; // 만약 o가 n이면 반복문의 처음으로 돌아감
        else
            printf("잘못된 입력입니다.\n"); // 그 외의 경우에는 잘못된 입력임을 알림
    }

    return 0;
}