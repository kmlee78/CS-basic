#include <studio.h>
#include <math.h>            // pow 함수를 사용하기 위해 math.h 헤더파일을 포함
#define SECOND_PER_MINUTE 60 // 60을 상수 SECOND_PER_MINUTE으로 정의

int main(void)
{
    int x = 1000;
    int mintue = x / SECOND_PER_MINUTE;
    int second = x % SECOND_PER_MINUTE;
    printf("%d분 %d초", mintue, second); // 16분 40초 출력

    x++;
    printf("%d", x);   // 1001 출력
    printf("%d", x--); // 1001 출력. 후위 감소 연산자는 해당 줄의 실행이 끝난 후에 x의 값을 1 감소시킴
    printf("%d", x);   // 1000 출력
    printf("%d", --x); // 999 출력. 전위 감소 연산자는 해당 줄의 실행이 끝나기 전에 x의 값을 1 감소시킴

    int a = 10, b = 20;
    printf("%d", a == b);              // 0 출력. a와 b가 같지 않으므로 0이 출력됨
    printf("%d", a != b);              // 1 출력. a와 b가 같지 않으므로 1이 출력됨
    printf("%d", (a < b) && (b < 40)); // 1 출력. a가 b보다 작고 b가 40보다 작으므로 1이 출력됨
    printf("%d", (a < b) || (b > 40)); // 1 출력. a가 b보다 작으므로 1이 출력됨

    int i = -50, j = 60;
    int absolute_i = (i > 0) ? i : -i; // i가 양수면 i를, 음수면 -i를 absolute_i에 저장
    int max = (i > j) ? i : j;         // i가 j보다 크면 i를, 아니면 j를 max에 저장

    double q = pow(2.0, 20.0);
    printf("%.0f", q); // 1048576 출력. pow(2.0, 20.0)은 2의 20제곱을 의미함

    return 0;
}