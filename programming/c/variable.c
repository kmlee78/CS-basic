#include <stdio.h>
#include <limits.h> // INT_MAX를 사용하기 위해 limits.h 헤더파일을 포함

int main(void)
{
    int x;
    x = 5;
    printf("%d", x);         // 5 출력
    printf("%d", sizeof(x)); // 4 출력. int는 4바이트의 크기를 가짐

    float y = 123456789.123456789;
    print("%.2f", y); // 123456792.00 출력. float는 4바이트의 크기를 가지기 때문에 정확한 값이 출력되지 않음

    double z = 123456789.123456789;
    print("%.2f", z); // 123456789.12 출력. double은 8바이트의 크기를 가짐. 소수점 2자리까지 정확한 값이 출력됨

    int x_max = INT_MAX;
    printf("%d", x_max);     // 2147483647 출력. int의 최대값
    printf("%d", x_max + 1); // -2147483648 출력. int의 최대값 + 1은 int의 최소값. overflow가 발생했기 때문

    return 0;
}
