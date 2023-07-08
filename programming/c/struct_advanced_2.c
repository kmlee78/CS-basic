#include <stdio.h>
#define SIZE 5

struct student
{
    int number;
    char name[20]; // 한글은 10자까지 가능
    double grade;
};

int main(void)
{
    struct student list[SIZE]; // 구조체 배열 선언
    int i;
    for (i = 0; i < SIZE; i++)
    {
        printf("학번을 입력하세요: ");
        scanf("%d", &list[i].number);
        printf("이름을 입력하세요: ");
        scanf("%s", list[i].name);
        printf("학점을 입력하세요: ");
        scanf("%lf", &list[i].grade); // double은 %lf로 입력받는다.
    }
    for (i = 0; i < SIZE; i++)
    {
        printf("학번: %d, 이름: %s, 학점: %.1f\n", list[i].number, list[i].name, list[i].grade);
    }

    return 0;
}