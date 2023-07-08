#include <stdio.h>

// 두 변수의 값을 서로 변환하는 포인터 함수
void swap(int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

int main(void)
{
    int a = 10;
    int *b = &a;
    printf("a = %d, *b = %d", a, b);  // a = 10, *b = 10, a와 *b는 같은 값
    printf("&a = %p, b = %p", &a, b); // &a = 0x7ffeeb0b0a3c, b = 0x7ffeeb0b0a3c, a와 *b는 같은 값
    int x = 1;
    int y = 2;
    swap(&x, &y);
    printf("x = %d, y = %d\n", x, y); // x = 2, y = 1

    // 포인터 변수의 값을 바꾸면 원래 변수의 값도 바뀐다.
    int i = 10;
    int *p;
    p = &i;
    printf("i = %d", i); // i = 10
    *p = 20;
    printf("i = %d", i); // i = 20

    return 0;
}