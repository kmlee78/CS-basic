#include <stdio.h>
#include <stdlib.h>

struct Book
{
    int number;
    char title[100];
};

// Book 구조체 내의 number와 title 멤버를 출력하는 함수
void showBook(struct Book *p, int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d: %s\n", (p + i)->number, (p + i)->title);
    }
}

int main(void)
{
    /* 동적 메모리를 이용한 구조체 */
    struct Book *p;
    p = (struct Book *)malloc(2 * sizeof(struct Book)); // 구조체 2개를 저장할 수 있는 메모리를 할당한다.
    if (p == NULL)
    {
        printf("동적 메모리 할당에 실패했습니다.");
        exit(1);
    }
    p->number = 1;                            // 포인터 p가 가리키는 구조체의 number 멤버에 1을 저장한다.
    strcpy(p->title, "C Programming");        // 포인터 p가 가리키는 구조체의 title 멤버에 C Programming을 저장한다.
    (p + 1)->number = 2;                      // 포인터 p가 가리키는 구조체의 다음 구조체의 number 멤버에 2를 저장한다.
    strcpy((p + 1)->title, "Data Structure"); // 포인터 p가 가리키는 구조체의 다음 구조체의 title 멤버에 Data Structure를 저장한다.
    showBook(p, 2);                           // 1: C Programming, 2: Data Structure
    free(p);

    return 0;
}