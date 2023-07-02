#include <studio.h>

int main(void)
{
    char x = 'A';    // 하나의 문자를 저장하기 위해 char 자료형을 사용
    printf("%c", x); // A 출력. char는 1바이트의 크기를 가짐
    char y = 65;
    printf("%c", y); // A 출력. 아스키 코드 65는 문자 A와 같음. 출력 시 %c를 사용하면 문자로 출력됨
    char z = 'B';
    printf("%d", z); // 66 출력. 아스키 코드 66은 문자 B와 같음. 출력 시 %d를 사용하면 정수로 출력됨

    int a = 100;
    printf("%o", a); // 144 출력. 8진수로 출력됨
    printf("%x", a); // 64 출력. 16진수로 출력됨

    return 0;
}